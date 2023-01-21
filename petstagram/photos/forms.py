from django import forms

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.core.form_mixin import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        labels = {
            'photo': 'Photo file',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag pets',
        }


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('photo', 'publication_date')


class PhotoDeleteForm(DisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('photo', 'description', 'location', 'tagged_pets')

    disabled_fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()
            Photo.objects.all().first().tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            # self.instance.save()
            self.instance.delete()

        return self.instance

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #
    #     return self.instance
    #
    # def clean_tagged_pets(self):
    #     tagged_pets = self.cleaned_data['tagged_pets']
    #     if tagged_pets:
    #         self.instance.tagged_pets.unset(self.instance)
    #
    #     return []
