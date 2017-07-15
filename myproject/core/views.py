from django.shortcuts import render
from .models import Contact


def home(request):
    contacts = Contact.objects.all()
    ctx = {
        'contacts': contacts,
    }
    return render(request, 'index.html', ctx)
