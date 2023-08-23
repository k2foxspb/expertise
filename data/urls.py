from django.urls import path

from data import views
from data.apps import DataConfig
from data.views import DataView

app_name = DataConfig.name

urlpatterns = [
    path('', DataView.as_view(), name='data'),
    path("create/", views.create),

]
