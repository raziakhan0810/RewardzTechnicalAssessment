"""book_rental URL Configuration
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', include('rental.urls')),
]
