from django import forms

from petstagram.core.form_mixin import DisabledFormMixin
from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'name',
            'date_of_birth',
            'personal_pet_photo',
        )
        # exclude = ('slug',)
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_pet_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Pet name', }
            ),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'personal_pet_photo': forms.TextInput(
                attrs={'placeholder': 'Link to image'}
            ),
        }


class PetEditForm(PetForm):
    pass


class PetDeleteForm(DisabledFormMixin, PetForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_pet_photo')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
