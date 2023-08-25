from django.urls import path

from data import views
from data.apps import DataConfig
from data.views import DataView

app_name = DataConfig.name

urlpatterns = [
    path('', DataView.as_view(), name='data'),
    path("create/", views.DataCreateView.as_view(), name='create'),
    path("edit/<int:pk>/", views.DataUpdateView.as_view(), name='edit'),
    path("delete/<int:pk>/", views.DataDeleteView.as_view(), name='delete'),

]
