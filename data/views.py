from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from data.models import Data
from django_comments.moderation import CommentModerator, moderator


# Create your views here.
class DataView(PermissionRequiredMixin, ListView):
    model = Data

    template_name = 'data.html'
    permission_required = ("data.add_data",)
    permission_denied_message = 'неть'

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class DataCreateView(PermissionRequiredMixin, CreateView):
    model = Data
    fields = '__all__'
    success_url = reverse_lazy("data:data")
    permission_required = ("data.add_data",)
    template_name = 'data.html'


class DataUpdateView(PermissionRequiredMixin, UpdateView):
    model = Data
    fields = '__all__'
    success_url = reverse_lazy("data:data")
    permission_required = ("data.change_data",)
    template_name = 'data_form.html'


class DataDeleteView(PermissionRequiredMixin, DeleteView):
    model = Data
    success_url = reverse_lazy("data:data")
    permission_required = ("data.delete_data",)
    template_name = 'data_confirm_delete.html'


class DataModerator(CommentModerator):
    email_notification = True
    enable_field = 'deleted'


moderator.register(Data, DataModerator)
