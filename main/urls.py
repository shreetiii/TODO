from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/',views.home),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add-todo'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit-todo'),
    path('complete/<int:id>/', views.complete, name='complete-todo')


]