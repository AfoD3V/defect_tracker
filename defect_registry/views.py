from django.shortcuts import render, HttpResponse


# Create your views here.
def defect_home_page(request):
    return HttpResponse("This is main page.")
