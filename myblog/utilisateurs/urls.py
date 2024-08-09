from django.urls import path
from .views import loginview
from django.contrib.auth.views import LogoutView
from .views import register_user


urlpatterns = [
    path('login/', loginview, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register'),

]