from django.shortcuts import render, HttpResponse
from .models import Profile


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


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    context = {
        "user_profile": user_profile,
    }
    return render(request, "pdf/resume.html", context)
