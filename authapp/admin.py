from django.contrib import admin

from authapp import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
    # list_filter = ('id', 'date_joined')




