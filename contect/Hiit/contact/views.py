from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')

        if name and subject and message and email:
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email= 'gpwork729@gmail.com',
                    recipient_list=[email]
                )
                return HttpResponse("Email sent successfully!")
            except Exception as e:
                return HttpResponse(f"Failed to send email: {e}")
        return HttpResponse("All fields are required.")
    return render(request, 'emaiil.html')
