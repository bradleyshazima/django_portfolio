from django.shortcuts import render
from .forms import ContactForm
from .models import About
from .models import Contact

# Create your views here.

def landing(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  # Handle success message or redirection if needed
    else:
        form = ContactForm()

    about = About.objects.first()  # Fetch the first record of About
    contact = Contact.objects.first()
    return render(request, 'landing.html', {'form': form, 'about': about, 'contact': contact})

def resume(request):
    return render(request, 'resume.html')
