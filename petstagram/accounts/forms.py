from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.views.generic import UpdateView

UserModel = get_user_model()


class RegisterPetstagramUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)
        field_classes = {'username': UsernameField}


# class EditPetstagramUserForm():
#     class Meta:
#         model = UserModel
#         fields = ('first_name', 'last_name', 'username', 'email', 'profile_picture', 'gender',)
#         labels = {
#             'first_name': 'First name',
#             'last_name': 'Last name',
#             'username': 'Username',
#             'email': 'Email',
#             'profile_picture': 'Image',
#             'gender': 'Gender',
#         }



