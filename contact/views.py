from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

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

