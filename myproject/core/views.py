from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def home(request):
    contacts = Contact.objects.all()
    ctx = {
        'contacts': contacts,
        'contact_form': ContactForm
    }
    return render(request, 'index.html', ctx)


def contact_add(request):
    if request.is_ajax() and request.method == 'POST':
        form = ContactForm(request.POST)
        if not form.is_valid():
            error = {'error': form.errors}
            return JsonResponse(error, status=422)

        treatment = request.POST.get('treatment')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        f = form.save()
        name = [f.get_treatment_display(), f.first_name, f.last_name]
        name = ' '.join(filter(None, name))
        ctx = {
            'name': name,
            'email': f.email,
            'phone': f.phone,
        }
        return JsonResponse(ctx)
    else:
        messages.error(request, 'Favor preencher o nome do contato.')
        return HttpResponseRedirect(reverse('home'))
