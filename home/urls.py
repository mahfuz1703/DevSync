from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',  home, name='home'),
    path('login/', loginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='signout'),
    path('signup/', registerView.as_view(), name='signup'),
]