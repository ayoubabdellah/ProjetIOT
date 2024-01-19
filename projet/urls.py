from django.contrib import admin
from django.urls import path, include

from DHT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DHT.urls')),
]
