from django.shortcuts import render

from projects.models import Project, Skill


def index(request):
    projectSet = Project.objects.all().order_by("-dateAdded")
    general = Skill.objects.all().filter(general=True)

    context = {"prgSet": projectSet, "generalSkills": general}
    return render(request, "pages/index.html", context)
