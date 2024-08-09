from django.urls import path
from .views import home ,contact,about,contact_detail,contact_create,edit_contact,delte_contact


urlpatterns=[
    path("",home, name="index"),
    path("about/",about, name="about"),
    path("contact/",contact , name="contact"),
    path("contact/create/",contact_create, name="contact_create"),
    path("contact/<int:id>",contact_detail, name="contact_detail"),
    path("contact/edit/<int:id>",edit_contact, name="edit_contact"),
    path("contact/delete/<int:id>",delte_contact, name="delete_contact"),
    
]