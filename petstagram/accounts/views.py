from django.contrib.auth import get_user_model, views as auth_views, login, authenticate
from django.core.paginator import Paginator

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_view

from petstagram.accounts.forms import RegisterPetstagramUserForm

UserModel = get_user_model()


class RegisterUserView(generic_view.CreateView):
    form_class = RegisterPetstagramUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #
    #     login(request, self.object)
    #
    #     return response
    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class DetailsUserView(generic_view.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    photos_paginate_by = 3

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()
        photos = self.object.photo_set.order_by('-publication_date')

        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # is_owner = self.req.user(login user) == self.object(is the user of DetailView)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        # context['photos_count'] = self.object.photo_set.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        context['photos'] = self.get_paginated_photos()

        return context


class EditUserView(generic_view.UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'
    fields = ('first_name', 'last_name', 'email', 'profile_picture', 'gender',)
    context_object_name = object
    print(object)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class DeleteUserView(generic_view.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


"""
tedy123456
"""