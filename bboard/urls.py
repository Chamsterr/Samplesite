from django.urls import path, include

from .views import index

urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('', index),
]