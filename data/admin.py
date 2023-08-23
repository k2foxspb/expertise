from django.contrib import admin

from data import models


# Register your models here.
@admin.register(models.Data)
class ServicesAdmin(admin.ModelAdmin):
    search_fields = ["id"]
