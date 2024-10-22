from django.urls import path
from postgre import views

urlpatterns = [
    path('', views.index),

]
