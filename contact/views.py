from django.shortcuts import render
from .forms import ContactForm

def index(request):
    context={'form':ContactForm()}
    return render(request, 'index.html', context)


def add_contact(request):
    if request.method == 'POST':
        pass
    context={'form':ContactForm()}
    return render(request, 'partials/form.html', context)

