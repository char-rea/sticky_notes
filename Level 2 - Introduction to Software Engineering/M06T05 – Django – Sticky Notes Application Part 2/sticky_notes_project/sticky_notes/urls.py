from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the entire project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]