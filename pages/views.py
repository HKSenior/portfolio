from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from decouple import config

from projects.models import Project, Skill
from contact.models import Contact
from contact.forms import ContactForm


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request):
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

        form = ContactForm()
        formUrl = config('FORM_URL')

        context = {
            "form": form,
            "formUrl": formUrl,
            "prgSet": projectSet,
            "generalSkills": general,
            "langSpecificSkills": langSpecificSkillsDict
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phoneNumber']
            message = form.cleaned_data['message']

            contact = Contact(
                name=name,
                email=email,
                phoneNumber=phoneNumber,
                message=message
            )
            contact.save()

            subject = 'hassaniprojects.com - Inquiry'
            from_email = config('DEFAULT_FROM_EMAIL')
            to_email = [config('EMAIL_PERSONAL')]
            message = """
            name - {}
            email - {}
            phoneNumber - {}
            message - {}""".format(
                name,
                email,
                phoneNumber,
                message
            )

            _ = send_mail(
                subject,
                message,
                from_email,
                to_email,
                fail_silently=config('EMAIL_FAIL_SILENTLY', cast=bool)
            )

            if _ == 1:
                messages.success(
                    request,
                    "Thank you and I will get back to you as soon as possible."
                )
            elif _ == 0:
                messages.error(
                    request,
                    "A problem occured while submitting the form. Please feel "
                    "free to send me a direct email to "
                    + config('EMAIL_PERSONAL')
                )
            return redirect('index')
        else:
            messages.error(
                request,
                "A problem occured while submitting the form. Feel "
                "free to send me a direct email to "
                + config('EMAIL_PERSONAL')
            )
            return redirect('index')
