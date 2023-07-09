from django.urls import path

from services import views
from services.apps import ServicesConfig

app_name = ServicesConfig.name

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services'),
    path("create/", views.ServicesCreateView.as_view(), name="services_create"),
    path(
        "services/<slug:slug>/",
        views.ServicesDetailView.as_view(),
        name="services_detail",
    ),
    path(
        "services/<slug:slug>/update",
        views.ServicesUpdateView.as_view(),
        name="services_update",
    ),
    path(
        "services/<slug:slug>/delete",
        views.ServicesDeleteView.as_view(),
        name="services_delete",
    ),
]
