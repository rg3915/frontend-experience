from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


def home(request):
    contacts = Contact.objects.all()
    ctx = {
        'contacts': contacts,
        'contact_form': ContactForm
    }
    return render(request, 'index.html', ctx)
