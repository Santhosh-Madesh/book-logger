from django.urls import path
from .views import home, add, about

urlpatterns=[
    path("",home,name="home"),
    path("add/",add,name="add"),
    path("about/",about,name="about"),
]