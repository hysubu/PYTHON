from django.urls import path
from . import  views

urlpatterns = [
    path('data/',views.data,name="data"),
    path('data2/',views.data2,name="data2"),
    path('about/',views.about,name="about")
]