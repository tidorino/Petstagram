from django.contrib.auth import admin as auth_admin, get_user_model

from django.contrib import admin


from petstagram.accounts.forms import RegisterPetstagramUserForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(auth_admin.UserAdmin):

    form = UserEditForm
    add_form = RegisterPetstagramUserForm

    list_filter = ("is_staff", "is_superuser",)

    fieldsets = (
        (None,
         {'fields': (
             'username',
             'password',
         )
         }
         ),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'profile_picture',
                    'gender',
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields':
                    (
                        'last_login',
                        'date_joined'
                    )
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes':
                    (
                        'wide',
                    ),
                'fields':
                    (
                        'username',
                        'password1',
                        'password2',
                    ),
            },
        ),
    )
