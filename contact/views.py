from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm
from .models import Contact
from django.views.decorators.http import require_http_methods


def index(request):
    context = {'form':ContactForm(), 'contacts':Contact.objects.all()}
    return render(request, 'index.html', context)


def add_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save()
            return render(request, 'partials/contact.html', {'contact':contact})
    return render(request, 'partials/form.html', {'form':form})



@require_http_methods(['DELETE'])
def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete'
    return response

