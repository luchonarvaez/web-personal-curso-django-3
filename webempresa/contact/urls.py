from django.urls import path
from . import views

urlpatterns = [
    # path del core app
    path('',views.contact,name='contact'),
]
