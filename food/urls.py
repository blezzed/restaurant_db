from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('food/', views.getFoods),
    path('food/create/', views.createFood),
    path('food/<str:pk>/update', views.updateFood),
    path('food/<str:pk>/delete', views.deleteFood),
    path('food/<str:pk>/', views.getFood),
]