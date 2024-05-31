from django.shortcuts import render, HttpResponse


# Create your views here.
def resume(request):
    return render(request, "resume.html")
