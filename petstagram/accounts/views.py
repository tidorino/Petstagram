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


class DetailsUserView(generic_view.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # is_owner = self.req.user(login user) == self.object(is the user of DetailView)
        context['is_owner'] = self.request.user == self.object

        return context


class EditUserView(generic_view.UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'
    fields = ('first_name', 'last_name', 'email', 'gender',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class DeleteUserView(generic_view.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


