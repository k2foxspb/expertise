from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email, firs_name, last_name):
    """Sends an email when the feedback form has been submitted."""
    sleep(2)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Your Feedback",
        f"\t{firs_name}{last_name}\n\nThank you for registrations!",
        "k2foxspb@mail.ru",
        ['k2foxspb@gmail.com', email],
        fail_silently=False,
    )
