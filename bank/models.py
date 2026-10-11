from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Check(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    account_number = models.IntegerField()
    money = models.IntegerField()

    def __str__(self):
        return f"{self.title} — {self.author}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)]
    )

    def __str__(self):
        return f"{self.title} — {self.author}"
