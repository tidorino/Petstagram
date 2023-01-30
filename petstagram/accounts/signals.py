from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_registration(instance, created, **kwargs):
    if not created:
        return

    send_mail(
        subject='Wellcome to Petstagram!',
        html_message = render_to_string('successful_register_email/email-greeting.html',
                                        {'profile': instance}),
        message='You just register!',
        from_email=None,
        recipient_list=(instance.email,),
    )
