from celery import shared_task

from .utils import imageBuilder
from .svg import mergeAllImages


@shared_task
def render_image(count: int):
    return mergeAllImages(imageBuilder(count)).getvalue()
