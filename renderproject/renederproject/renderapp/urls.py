
from django.urls import path

from renderapp import views

urlpatterns = [
    path('',views.demo, name='demo')
]
