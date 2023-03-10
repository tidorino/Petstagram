from django.urls import path, include

from petstagram.accounts.views import RegisterUserView, LoginUserView, LogoutUserView,\
    EditUserView, DetailsUserView, DeleteUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', DetailsUserView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
)
#
# from .signals import *
