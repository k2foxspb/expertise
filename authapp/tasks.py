from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        'test',
        'hello',
        email,
        ['k2foxspb@mail.ru'],
        fail_silently=False,

    )
