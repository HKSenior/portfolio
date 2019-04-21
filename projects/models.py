from django.db import models


class PorjectModel(models.Model):
    title = models.CharField(max_length=100)
    techUsed = models.TextField()
    description = models.TextField()
    github = models.URLField()
    url = models.URLField()
    dateAdded = models.DateField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
