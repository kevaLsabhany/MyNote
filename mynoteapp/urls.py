from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('Add-Note',views.addNote,name="addNote"),
    path('<int:id>/Delete-Note',views.deleteNote,name="deleteNote"),
]