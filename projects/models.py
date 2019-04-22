from django.db import models


class Skill(models.Model):
    PYTHON = "PY"
    CPP = "CPP"
    C = "C"
    JAVASCRIPT = "JS"
    TYPESCRIPT = "TS"
    HTML = "HTML"
    CSS = "CSS"
    LANGUAGES = (
        (PYTHON, "Python"),
        (CPP, "C++"),
        (C, "C"),
        (JAVASCRIPT, "JavaScript"),
        (TYPESCRIPT, "TypeScript"),
        (HTML, "HTML"),
        (CSS, "CSS"),
    )

    skill = models.CharField(max_length=100)
    language = models.CharField(
        max_length=4, choices=LANGUAGES, default=PYTHON, blank=True
    )
    general = models.BooleanField(default=False)

    def __str__(self):
        return self.skill


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github = models.URLField()
    url = models.URLField()
    dateAdded = models.DateField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skill, related_name="skills")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("lastModified",)
