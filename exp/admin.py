from django.contrib import admin
from exp import models as exp_models


@admin.register(exp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]