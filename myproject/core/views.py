from django.shortcuts import render


def home(request):
    contacts = Contact.objects.all()
    ctx = {
        'contacts': contacts,
    }
    return render(request, 'index.html', ctx)
