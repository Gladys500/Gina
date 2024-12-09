from django.contrib import admin
from .models import RestaurantInfo, MenuItem, Chef, Event, Booking, Gallery, Testimonial, ContactRequest

# Register your models here.

# Restaurant Info Admin
@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'address', 'email')

# Menu Admin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('item_name', 'category')

# Chef Admin
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

# Event Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

# Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests')
    search_fields = ('name', 'email')
    list_filter = ('date', 'time')

# Gallery Admin
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

# Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'date')
    list_filter = ('rating', 'date')
    search_fields = ('name',)

# Contact Request Admin
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_submitted')
    search_fields = ('name', 'email')
    list_filter = ('date_submitted',)
