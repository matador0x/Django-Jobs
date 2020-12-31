from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contactForm(request):

    

    if request.method == "POST":
        email   = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
        subject,
        message,
        email,
        [settings.EMAIL_HOST_USER],
        )
    return render(request,"contact/contact.html")