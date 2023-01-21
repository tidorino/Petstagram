from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication_date', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        tagged_pets = obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'

