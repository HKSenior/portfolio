from django.contrib import admin

from .models import PorjectModel


@admin.register(PorjectModel)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "github",
        "url",
        "dateAdded",
        "lastModified",
    )
    search_fields = ("id", "title", "dateAdded")
    list_per_page = 10
