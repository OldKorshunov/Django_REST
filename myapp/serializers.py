from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorsBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id',]


class BookAuthorAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'slug', 'title',]
