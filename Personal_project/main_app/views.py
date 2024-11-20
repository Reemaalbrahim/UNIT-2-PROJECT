from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Message  
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from django.conf import settings



def home_view(request):
    return render(request, 'main_app/home.html')



def contact_view(request):

   if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        if not Message.objects.filter(first_name=first_name, last_name=last_name, email=email,message=message).exists():
            new_message = Message(first_name=first_name, last_name=last_name, email=email,message=message)
            new_message.save()

            messages.success(request, "Your message has been sent successfully!")

            #send confirmation email 
            content_html= render_to_string("main_app/mail/confirmation.html")
            send_to=email
            email_message= EmailMessage("Confirmation Message",content_html, settings.EMAIL_HOST_USER, [send_to])
            email_message.content_subtype ="html"
            email_message.send()

            content_html= f"user {first_name} {last_name} contacted you." + f"<br/> {message}"
            send_to=email
            email_message= EmailMessage("Confirmation",content_html, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            email_message.content_subtype ="html"
            email_message.send()
            #


        else:
            messages.info(request, "It seems you've already submitted this message.")


        return redirect("main_app:contact_view")
   
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