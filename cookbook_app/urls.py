from cookbook_app import views
from django.urls import path

urlpatterns = [
    path('', views.recipe),
    path('recipe/', views.detailRecipe)
]