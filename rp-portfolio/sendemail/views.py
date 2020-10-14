from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)

        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])

            f.save()
            return redirect('submitted')
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f})

def submitted(request):
    return render(request,'success.html')
