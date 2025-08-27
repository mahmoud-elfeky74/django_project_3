from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'new/home.html',{'contacts':Contact.objects.all()})
def services(request):
    return render(request,'new/services.html',{'contacts':Contact.objects.all()})
def about(request):
    return render(request,'new/about.html',{'contacts':Contact.objects.all()})
def contact(request):
    return render(request,'new/contact.html',{'contacts':Contact.objects.all()})