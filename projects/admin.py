from django.contrib import admin

from .models import Project, Skill


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "github",
        "url",
        "dateAdded",
        "lastModified",
        "Skills",
        "image",
    )
    search_fields = ("title", "dateAdded")
    list_filter = ("dateAdded", "lastModified")
    list_per_page = 15

    def Skills(self, obj):
        return ", ".join([str(s) for s in obj.skills.all()])


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("skill", "language", "general")
    search_fields = ("skill", "language", "general")
    list_filter = ("language", "general")
