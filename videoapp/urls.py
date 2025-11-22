from django.urls import path
from . import views

urlpatterns = [
    path('',views.helloworld,name="home"),
    path('video/<int:pk>',views.video,name="video"),
    path('search/',views.search,name="search")
]