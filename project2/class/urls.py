from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/', views.home, name='Home2'),
    url('register/', views.register, name='Register')
]