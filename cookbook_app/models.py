from django.db import models

class Recipe(models.Model):
    name = models.CharField('Название', max_length=60)
    img = models.ImageField(upload_to='RecipeMedia/', verbose_name='Foto')
    # instruction = models.TextField()

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return f"{self.name}"

class Articles(models.Model):
    title = models.CharField('Название', max_length=60)
    img = models.ImageField(upload_to='RecipeMedia/', verbose_name='Foto')

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.title}"

class Categories(models.Model):
    title = models.CharField('Название', max_length=60)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.title}"