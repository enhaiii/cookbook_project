from django.contrib import admin
from .models import *

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Categories)
admin.site.register(Step)
admin.site.register(User)
admin.site.register(Favorites)
admin.site.register(Comment)