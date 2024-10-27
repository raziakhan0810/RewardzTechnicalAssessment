from django.contrib import admin
from .models import Book, Rental


class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for Book model.
    """
    list_display = ('title', 'number_of_pages')
    search_fields = ('title',)


class RentalAdmin(admin.ModelAdmin):
    """
    Admin interface for Rental model.
    """
    list_display = ('user', 'book', 'rental_date', 'extended', 'fees')
    list_filter = ('extended',)
    search_fields = ('user__username', 'book__title')
    date_hierarchy = 'rental_date'

admin.register(Book, BookAdmin)
admin.register(Rental, RentalAdmin)