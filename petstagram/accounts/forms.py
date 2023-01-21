from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class RegisterPetstagramUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'
