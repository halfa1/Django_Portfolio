from django.shortcuts import render, redirect
from .forms import ContactForm

# View for the landing page
def index_view(request):
    return render(request, 'portfolio/index.html')

# View for the contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            return redirect('success')  # Redirect to success page after submission
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})

# Success page after form submission
def success_view(request):
    return render(request, 'portfolio/success.html')
