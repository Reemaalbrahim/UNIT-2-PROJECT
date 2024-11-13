from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Message  

def home_view(request):
    return render(request, 'main_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        
       
        Message.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)

        # Send email (optional)
        send_mail(
            f'Message from {first_name} {last_name}',
            message,
            email,
            ['your_email@example.com'],
            fail_silently=False,
        )
        return redirect('messages')

    return render(request, 'main_app/contact.html')

def messages_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        message = Message.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message_text
        )
        message.save()
        return redirect('main_app:messages_view')  # Redirect to the messages view after saving

    messages = Message.objects.all()
    return render(request, 'main_app/messages.html', {'messages': messages})


def resume_view(request):
    return render(request, 'main_app/resume.html')

