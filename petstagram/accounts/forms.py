from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.views.generic import UpdateView

UserModel = get_user_model()


class RegisterPetstagramUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)
        field_classes = {'username': UsernameField}





