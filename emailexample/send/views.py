from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail(
        'Hello from Arequipa', 
        'Hello there. This is an automated message.',
        'salasvictor123@hotmail.com',
        ['secejap327@fna6.com'],
        fail_silently=False
    )
    return render(request, 'send/index.html')