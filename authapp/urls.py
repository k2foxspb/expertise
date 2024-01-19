from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path

from authapp import views
from authapp.apps import AuthappConfig
from authapp.views import ResetPasswordView, ResetPasswordConfirmView

app_name = AuthappConfig.name

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         ResetPasswordConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path(
        "profile_edit/<int:pk>/",
        views.ProfileEditView.as_view(),
        name="profile_edit",
    ),
]
