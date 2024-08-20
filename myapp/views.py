from django.shortcuts import render
from django.http import HttpResponse
from .models import Abc
from .models import Calander
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def Home(request):
    return render(request,'Home.html',{})

def loginData(request):
    name = request.POST.get('name','default')    
    mobile = request.POST.get('mobile','default')    
    email = request.POST.get('email','default')    
    print(name,mobile,email)

    A = Abc(name=name,mobile=mobile,email=email)
    A.save()

    subject = 'welcome to contact data'
    message = 'Hi everyone, thank you for registering in contact data.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['divyanshc494@gmail.com']
    send_mail( subject, message, email_from, recipient_list )


    return HttpResponse("Massage send succefully......")

def calanderData(request):
    calander = request.POST.get('calander','default')
    # dropdown = request.POST.get('dropdown','default')
    print(calander)

    B = Calander(calander=calander)
    B.save()
 
    

    return HttpResponse("Your Booking Date is Confrim..... <br> So Please Fill your registation form....If you already filled the form So please ignore this msg ")