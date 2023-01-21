from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as generic_view

UserModel = get_user_model()


class RegisterUserView(generic_view.CreateView):
    model = UserModel
    template_name = 'accounts/register-page.html'


def login_user(request):
    return render(request, 'accounts/login-page.html')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def user_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
