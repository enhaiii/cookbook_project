from django.shortcuts import render, get_object_or_404
from .models import *

def recipe(request):
    context = {

    }
    return render(request, 'main.html', context)

def detailRecipe(request):
    context = {

    }
    return render(request, 'recipe.html', context)
