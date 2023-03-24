import os

from django.conf import settings

def imageBuilder(number: int) -> list[str]:
    file_path = os.path.join(settings.STATIC_ROOT, 'image_backend', 'images')
    numbers_str = str(number).zfill(settings.MAX_DIGITS)
    numbers_path = []
    for number in numbers_str:
        for file in os.listdir(file_path):
            if file.startswith(number):
                numbers_path.append(os.path.join(file_path, file))
    return numbers_path

