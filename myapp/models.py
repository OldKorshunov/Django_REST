from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.urls import reverse_lazy


class Author(models.Model):
    slug = models.SlugField(
        blank=True,
        editable=False,
        max_length=128,
        unique=True, )
    name = models.CharField(max_length=120, verbose_name='author name')
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    slug = models.SlugField(
        blank=True,
        editable=False,
        max_length=128,
        unique=True,)

    title = models.CharField(blank=True, max_length=120)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        related_name='books',
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("book:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.title = self.title + '!'
        super(Book, self).save(*args, **kwargs)

