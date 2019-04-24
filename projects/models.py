from django.db import models


class Skill(models.Model):
    LANG_SHORT_HAND = {
        'PYTHON': "PY",
        'CPP': "CPP",
        'C': "C",
        'JAVASCRIPT': "JS",
        'TYPESCRIPT': "TS",
        'HTML': "HTML",
        'CSS': "CSS"
    }
    LANGUAGES = (
        (LANG_SHORT_HAND['PYTHON'], "Python"),
        (LANG_SHORT_HAND['CPP'], "C++"),
        (LANG_SHORT_HAND['C'], "C"),
        (LANG_SHORT_HAND['JAVASCRIPT'], "JavaScript"),
        (LANG_SHORT_HAND['TYPESCRIPT'], "TypeScript"),
        (LANG_SHORT_HAND['HTML'], "HTML"),
        (LANG_SHORT_HAND['CSS'], "CSS"),
    )

    skill = models.CharField(max_length=100)
    language = models.CharField(
        max_length=4,
        choices=LANGUAGES,
        default=LANG_SHORT_HAND['PYTHON'],
        blank=True
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
    image = models.ImageField(upload_to="%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("lastModified",)
