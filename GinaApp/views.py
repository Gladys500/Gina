from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'bookatable.html')

def chefs_page(request):
    return render(request, 'Chefs.html')

def contact(request):
    return render(request, 'contactpage.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def menu(request):
    return render(request, 'menu.html')

def testimonials(request):
    return render(request, 'testimonials.html')