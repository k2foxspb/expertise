from django.contrib import admin
from exp import models as exp_models
from services import models as services


@admin.register(exp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preamble", "body", "image"]


@admin.register(services.Services)
class ServicesAdmin(admin.ModelAdmin):
    search_fields = ["title"]


