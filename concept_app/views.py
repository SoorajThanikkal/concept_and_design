from django.shortcuts import render
from .import models

# Create your views here.
def index(request):
    proj= models.Projects.objects.all()
    return render(request,'index.html',{"proj":proj})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            message = data.get("message")

            email_subject = "New Message from Contact Form"
            email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"

            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                ['conceptdesignbuild.in@gmail.com','tpsooraj7@gmail.com'],
                fail_silently=False,
            )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})
# In your views.py
from django.http import Http404, HttpResponse
from django.conf import settings
import os

def serve_media(request, path):
    if not settings.DEBUG:
        media_root = settings.MEDIA_ROOT
        file_path = os.path.join(media_root, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read())
                # Set appropriate content type
                if path.endswith('.jpg') or path.endswith('.jpeg'):
                    response['Content-Type'] = 'image/jpeg'
                elif path.endswith('.png'):
                    response['Content-Type'] = 'image/png'
                return response
    raise Http404