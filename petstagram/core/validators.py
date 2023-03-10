from django.core.exceptions import ValidationError
from petstagram.core.utils import megabytes_to_bytes


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Name should contain only letters!')
    return value


def validate_max_image_size(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')