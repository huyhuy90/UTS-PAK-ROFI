from django.urls import path
from . import views

urlpatterns = [
    path('negara/', views.negara, name='negara'),
]