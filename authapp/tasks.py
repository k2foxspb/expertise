from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email, username):
    """Sends an email when the feedback form has been submitted."""

    send_mail(
        'привет от экспертов',
        f'новый пользователь  {email}{username}',
        'k2foxspb@mail.ru',
        ['k2foxspb@mail.ru'],
        fail_silently=False,
    )
