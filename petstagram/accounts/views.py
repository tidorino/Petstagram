from django.contrib.auth import get_user_model, views as auth_views

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_view

from petstagram.accounts.forms import RegisterPetstagramUserForm

UserModel = get_user_model()


class RegisterUserView(generic_view.CreateView):
    form_class = RegisterPetstagramUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def user_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
