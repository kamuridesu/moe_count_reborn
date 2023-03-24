
from django.http import HttpResponseNotFound, StreamingHttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from .models import User
from .tasks import render_image
from celery.result import AsyncResult


def stream_svg(task_id):
    result = AsyncResult(task_id)
    while not result.ready():
        yield ""
    svg = result.get()
    yield svg


def index(request: HttpRequest):
    username = request.GET.get("username")
    if not username:
        return render(request, "404.html", {'message': 'Username is required!'}, status=404)
    user, _ = User.objects.get_or_create(name=username)
    task = render_image.delay(user.count)
    response = StreamingHttpResponse(stream_svg(task.id), content_type="image/svg+xml")
    user.count += 1
    user.save()
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Vary'] = 'Accept-Encoding'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response["X-Accel-Buffering"] = "no"
    return response
