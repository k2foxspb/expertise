from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from exp import models as exp_models


class MainPageView(TemplateView):
    template_name = "exp/base.html"


class AboutUsView(TemplateView):
    template_name = "exp/aboutUs.html"


class OurEmployeesView(TemplateView):
    template_name = "exp/ourEmployees.html"


class NewsListView(ListView):
    model = exp_models.News
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = exp_models.News
    fields = "__all__"
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.add_news",)


class NewsDetailView(DetailView):
    model = exp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = exp_models.News
    fields = "__all__"
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = exp_models.News
    success_url = reverse_lazy("exp:news")
    permission_required = ("exp.delete_news",)
