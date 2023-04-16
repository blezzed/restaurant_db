from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('foods/', views.getFoods),
    path('foods/create/', views.createFood),
    path('foods/<str:pk>/update', views.updateFood),
    path('foods/<str:pk>/delete', views.deleteFood),
    path('foods/<str:pk>/', views.getFood),
]