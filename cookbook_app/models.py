from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Ingredient(models.Model):
    name = models.CharField('Название', max_length=60)
    default_unit = models.CharField('Единица измерения по умолчанию', max_length=10, default='г')
    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return f"{self.name}"
    
class Categories(models.Model):
    title = models.CharField('Название', max_length=60)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.title}"
    
class Recipe(models.Model):
    name = models.CharField('Название', max_length=60)
    img = models.ImageField(upload_to='RecipeMedia/', verbose_name='Foto', blank=True, null=True)
    description = models.CharField('Описание', max_length=500)
    timeCooking = models.IntegerField('Время готовки', help_text="Продолжительность в минутах")
    ingredient = models.ManyToManyField(Ingredient, through='RecipeIngredient', through_fields=('recipe', 'ingredient'), verbose_name='Ингредиенты')
    category = models.ManyToManyField(Categories, verbose_name='Категории')

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return f"{self.name}"
    
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps', verbose_name='Рецепт')
    order = models.PositiveSmallIntegerField('Порядковый номер', default=0)
    description = models.TextField('Описание шага')
    img = models.ImageField(upload_to='RecipeMedia/', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = "Шаг"
        verbose_name_plural = "Шаги"

    def __str__(self):
        return f"{self.id}", f"{self.name}"
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт', related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент', related_name='ingredient_recipes')
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=2,help_text='Количество ингредиента в рецепте')
    unit = models.CharField('Единица измерения', max_length=10, default='г', help_text='г, кг, мл, шт и т.д.')

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'
        unique_together = ['recipe', 'ingredient']
    
    def __str__(self):
        return f"{self.recipe.name}: {self.quantity} {self.unit} {self.ingredient.name}"
    
class User(models.Model):
    username = models.CharField('Имя', max_length=30)
    password = models.CharField('Пароль', max_length=20)
    avatar = models.ImageField(upload_to='UserMedia/', verbose_name='Foto', blank=True, null=True )
    birthday = models.DateField('Дата рождения')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.id}", f"{self.name}"

class Favorites(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by', verbose_name='Рецепт')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        unique_together = ['user', 'recipe']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} добавил {self.recipe.name} в избранное"

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments', verbose_name='Рецепт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    content = models.TextField('Текст комментария')
    rating = models.PositiveSmallIntegerField('Оценка (1-5)', null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.recipe.name}"