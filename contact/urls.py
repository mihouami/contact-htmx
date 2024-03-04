from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("add_contact/", add_contact, name='add-contact'),
    path("delete_contact/<int:pk>", delete_contact, name='delete_contact'),
]
