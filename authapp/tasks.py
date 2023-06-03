# import logging
# from django.contrib.auth import get_user_model
# from django.urls import reverse
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email):
    """Sends an email when the feedback form has been submitted."""

    send_mail(
        'привет',
        'hello',
        email,
        ['k2foxspb@mail.ru'],
        fail_silently=False,

    )


# @shared_task
# def send_verification_email(user_id):
#     UserModel = get_user_model()
#     try:
#         user = UserModel.objects.get(pk=user_id)
#         send_mail(
#             'Verify your QuickPublisher account',
#             'Follow this link to verify your account: '
#             'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )
#     except UserModel.DoesNotExist:
#         logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
