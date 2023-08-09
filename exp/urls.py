from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from exp import views
from exp.apps import ExpConfig
from exp.models import News

app_name = ExpConfig.name

info_dict = {
    "queryset": News.objects.all(),
    "date_field":  "updated",
}

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='about'),
    path('employees', views.OurEmployeesView.as_view(), name='employ'),
    path('news', views.NewsListView.as_view(), name='news'),
    path('work', views.AboutView.as_view(), name='aboutWork'),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"recipes": GenericSitemap(info_dict)}},
    ),
    path(
        "news/<slug:slug>/detail",
        views.NewsDetailView.as_view(),
        name="news_detail",
    ),
    path(
        "news/<slug:slug>/update",
        views.NewsUpdateView.as_view(),
        name="news_update",
    ),
    path(
        "news/<slug:slug>/delete",
        views.NewsDeleteView.as_view(),
        name="news_delete",
    ),
]
