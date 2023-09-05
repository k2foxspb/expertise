from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from exp import models as exp_models


class AboutUsView(TemplateView):
    template_name = "exp/aboutUs.html"


class OurEmployeesView(TemplateView):
    template_name = "exp/ourEmployees.html"


class AboutView(TemplateView):
    template_name = "exp/ourWork.html"


class NewsListView(ListView):
    model = exp_models.News
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = exp_models.News
    fields = ('title', 'preamble', 'body', 'image')
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.add_news",)


class NewsDetailView(DetailView):
    model = exp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = exp_models.News
    fields = ('preamble', 'body', 'deleted', 'image')
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = exp_models.News
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.delete_news",)


def tooLarge(request, exception):
    return render(request, 'includes/404.html')