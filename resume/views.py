from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Profile
import pdfkit
from django.template import loader
import io


# Create your views here.
def resume(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        summary = request.POST.get("summary")
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        university = request.POST.get("university")
        previous = request.POST.get("previous")
        skills = request.POST.get("skills")
        resume_profile = Profile(
            name=name,
            email=email,
            mobile_no=mobile_no,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous,
            skills=skills,
        )
        resume_profile.save()
    return render(request, "resume.html")


def generate_resume_pdf(request, id):
    user_profile = get_object_or_404(Profile, pk=id)
    template = loader.get_template("pdf/resume.html")
    html = template.render({"user_profile": user_profile})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"
    return response
