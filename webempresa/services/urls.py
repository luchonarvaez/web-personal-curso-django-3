from django.urls import path
from . import views

urlpatterns = [
    # path de services app
    path('',views.services,name='services'),
]
