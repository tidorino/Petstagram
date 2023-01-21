from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(auth_admin.UserAdmin):
    pass
