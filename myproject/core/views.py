from django.contrib import messages
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
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
            'id': f.id,
            'name': name,
            'email': f.email,
            'phone': f.phone,
        }
        return JsonResponse(ctx)
    else:
        messages.error(request, 'Favor preencher o nome do contato.')
        return HttpResponseRedirect(reverse('home'))


def contact_json(request, pk):
    contact = Contact.objects.filter(pk=pk)
    data = serializers.serialize('json', contact)
    return HttpResponse(data, content_type='application/json')


def contact_edit(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('contact_edit_id')
        contact = get_object_or_404(Contact, pk=pk)
        # Usando instance não precisa pegar os campos um a um.
        # form = CustomerForm(request.POST, instance=customer)

        # if not form.is_valid():
        #     error = {'error': form.errors}
        #     return JsonResponse(error, status=422)

        contact.treatment = request.POST.get('treatment')
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        response = {'status': 'update'}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect(reverse('home'))


def contact_delete(request, pk):
    if request.is_ajax() and request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        print(contact_id)
        contact = Contact.objects.get(pk=contact_id)
        contact.delete()
        ctx = {'status': 'Contato deletado com sucesso.'}
        return JsonResponse(ctx)
