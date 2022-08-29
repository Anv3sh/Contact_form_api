from http.client import HTTPResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

@csrf_exempt
def home(request):
    return render(request,'contact_form/pp.html')

@csrf_exempt
def contactform(request):
    if request.method=="POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")

        send_mail(
        'Thank you for contacting us.',
        f'Hey {name}!, Hope you are doing great! We have received your message and we will surely contact you back',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
        with open('contact_list.txt','w') as p:
            p.write(name+" ")
            p.write(email)
        data={
            "name":name,
            "email":email
        }
    return JsonResponse(data,safe=False)
