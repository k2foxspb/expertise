from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from services import models as services_model


class ServicesListView(ListView):
    model = services_model.Services
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class ServicesCreateView(PermissionRequiredMixin, CreateView):
    model = services_model.Services
    fields = ('title', 'body', 'image', 'price')
    success_url = reverse_lazy("services:services")
    permission_required = ("services.services_news",)


class ServicesDetailView(DetailView):
    model = services_model.Services


class ServicesUpdateView(PermissionRequiredMixin, UpdateView):
    model = services_model.Services
    fields = ('title', 'body', 'price', 'deleted', 'image')
    success_url = reverse_lazy("services:services")
    permission_required = ("services.change_services",)


class ServicesDeleteView(PermissionRequiredMixin, DeleteView):
    model = services_model.Services
    success_url = reverse_lazy("services:services")
    permission_required = ("services.delete_services",)
