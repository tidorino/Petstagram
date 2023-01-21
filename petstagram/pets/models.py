from django.core.validators import URLValidator
from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    MAX_LENGTH_NAME = 30

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False
    )

    personal_pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        # update
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Id:{self.id}- Name:{self.name}'
