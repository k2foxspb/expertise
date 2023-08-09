from django.urls import path

from exp import views
from exp.apps import ExpConfig

app_name = ExpConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='about'),
    path('employees', views.OurEmployeesView.as_view(), name='employ'),
    path('news', views.NewsListView.as_view(), name='news'),
    path('work', views.AboutView.as_view(), name='aboutWork'),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
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
