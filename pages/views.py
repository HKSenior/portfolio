from django.shortcuts import render

from projects.models import Project, Skill


def index(request):
    projectSet = Project.objects.all().order_by("-dateAdded")
    general = Skill.objects.all().filter(general=True)
    langSpecificSkillsSet = Skill.objects.all().filter(general=False)

    langSpecificSkillsDict = {}
    for k, v in Skill.LANG_SHORT_HAND.items():
        querySet = langSpecificSkillsSet.filter(language=v)
        if not querySet:
            pass
        else:
            langSpecificSkillsDict[k] = querySet

    context = {
        "prgSet": projectSet,
        "generalSkills": general,
        "langSpecificSkills": langSpecificSkillsDict
    }
    return render(request, "pages/index.html", context)
