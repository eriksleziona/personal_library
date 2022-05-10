from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f" Author {self.first_name} {self.last_name}"


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    isbn = models.BigIntegerField(max_length=1)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image_url = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', blank=True)
