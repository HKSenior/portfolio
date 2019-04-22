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
    )
    search_fields = ("title", "dateAdded")
    list_filter = ("dateAdded", "lastModified")
    list_per_page = 15

    def skills_display(self, obj):
        return ", ".join([str(s) for s in obj.skills.all()])

    # skills_display.short_description = "Skills"


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("skill", "language", "general")
    search_fields = ("skill", "language", "general")
    list_filter = ("language", "general")
