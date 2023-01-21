from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.validators import validate_only_letters


class ChoicesEnumMixIn:
    @classmethod
    def choices(cls):
        return [(g.name, g.value) for g in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixIn, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do Not Show'


class PetstagramUser(AbstractUser):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        null=False,
        blank=False,
    )
