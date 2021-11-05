from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        related_name='book',
    )