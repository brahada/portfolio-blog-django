from django.contrib import admin
from django.urls import path
from . import views
from .views import contact,submitted

urlpatterns = [
    path('', contact, name='contact'),
    path('submitted/', submitted, name='submitted'),
]
