from django.contrib import admin
from user.models import CustomUsers


@admin.register(CustomUsers)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    list_filter = ("email",)
    search_fields = ("email",)
