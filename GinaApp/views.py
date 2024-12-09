from tkinter.font import names

from django.shortcuts import render, redirect
from .models import Booking


# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

def booking(request):
    if request.method == 'POST':
        mybooking = Booking(
            name=request.POST.get('name'),
            email=request.POST.get('email'),  # Corrected: Changed parentheses to .get()
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            guests=request.POST.get('guests'),
            message=request.POST.get('message'),
        )

        mybooking.save()
        return redirect('/show')

    else:
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

def show(request):
    allbookings = Booking.objects.all()  # Retrieve all bookings from the database
    return render(request, 'show.html', {'Booking': allbookings})

def delete(request,id):
    book=Booking.objects.get(id=id)
    book.delete()
    return redirect('/show')