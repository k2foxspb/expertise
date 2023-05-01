from django.urls import path

from exp import views
from exp.apps import ExpConfig

app_name = ExpConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='about'),
    path('employees', views.OurEmployeesView.as_view(), name='employ'),
    path('news', views.NewsListView.as_view(), name='news'),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "news/<int:pk>/detail",
        views.NewsDetailView.as_view(),
        name="news_detail",
    ),
    path(
        "news/<int:pk>/update",
        views.NewsUpdateView.as_view(),
        name="news_update",
    ),
    path(
        "news/<int:pk>/delete",
        views.NewsDeleteView.as_view(),
        name="news_delete",
    ),
]
