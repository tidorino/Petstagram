from django.urls import path, include

from petstagram.accounts.views import login_user, delete_user, edit_user, register_user, user_details

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', user_details, name='details user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
)
