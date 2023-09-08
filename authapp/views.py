from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView
from authapp import forms


class CustomLoginView(LoginView):
    def form_valid(self, form):
        ret = super().form_valid(form)
        message = "Успешный вход!<br>Привет, %(username)s" % {
            "username": self.request.user.get_full_name()
            if self.request.user.get_full_name()
            else self.request.user.get_username()
        }
        messages.add_message(self.request, messages.INFO, mark_safe(f'{message}'))
        return ret

    def form_invalid(self, form):
        for _unused, msg in form.error_messages.items():
            messages.add_message(
                self.request,
                messages.WARNING,
                mark_safe(f"{msg}"),
            )
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("ещё увидимся!)"))
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    model = get_user_model()
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("services:services")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = forms.CustomUserChangeForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def test_func(self):
        return True if self.request.user.pk == self.kwargs.get("pk") else False

    def get_success_url(self):
        return reverse_lazy("authapp:profile_edit", args=[self.request.user.pk])


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "Мы отправили вам по электронной почте инструкции по установке пароля," \
                      "если существует учетная запись с указанным вами адресом электронной почты." \
                      "Вы должны получить их в ближайшее время." \
                      " Если вы не получили электронное письмо," \
                      "Пожалуйста, убедитесь, что вы ввели адрес, под которым зарегистрировались," \
                      "и проверьте папку со спамом"
    success_url = reverse_lazy('authapp:login')


class ResetPasswordConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    success_url = reverse_lazy('authapp:password_reset_complete')
