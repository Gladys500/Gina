from django.db import models

# Create your models here.
from django.db import models

# Restaurant Info
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    opening_hours = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Menu
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Appetizers', 'Appetizers'),
        ('Main Course', 'Main Course'),
        ('Desserts', 'Desserts'),
        ('Beverages', 'Beverages'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item_name

# Chefs
class Chef(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

# Events
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# Bookings
class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.name} on {self.date}"

# Gallery
class Gallery(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Gallery Image {self.id}"

# Testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Testimonial by {self.name}"

# Contact Requests
class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
