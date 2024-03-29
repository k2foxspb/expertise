import os

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from authapp.tasks import send_feedback_email_task, send_feedback_email_task_update


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "avatar",
        )
        field_classes = {"username": UsernameField}

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["first_name"],
            self.cleaned_data["last_name"]
        )

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data:
            if data < 18 or data > 90:
                raise ValidationError(_("Please, enter a valid age!"))
        return data


class CustomUserChangeForm(UserChangeForm):
    help_text = _('Пароли хранятся в зашифрованном виде, поэтому нет возможности посмотреть пароль)')

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",

        )
        field_classes = {"username": UsernameField}

    def clean_avatar(self):
        arg_as_str = "avatar"
        if arg_as_str in self.changed_data and self.instance.avatar:
            if os.path.exists(self.instance.avatar.path):
                os.remove(self.instance.avatar.path)
        return self.cleaned_data.get(arg_as_str)

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data:
            if data < 18 or data > 90:
                raise ValidationError(_("Please, enter a valid age!"))
        return data

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        send_feedback_email_task_update.delay(
            self.cleaned_data["email"], self.cleaned_data["first_name"],
            self.cleaned_data["last_name"]
        )

        # send_feedback_email_task.apply_async(args=[
        #     self.cleaned_data["email"], self.cleaned_data["message"]
        # ]
        # ) используется для точной настройки
