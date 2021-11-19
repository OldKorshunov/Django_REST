from django.utils.text import slugify
from rest_framework import status, response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer, AuthorsBookSerializer, BookAuthorAgeSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    lookup_field = "slug"
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        try:
            slug = slugify(request.data.get("name"))
            Author.objects.get(slug=slug)
            return Response("exists", status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def get_books(self, request, slug=None):
        author = self.get_object()
        books = Book.objects.filter(author=author.id).distinct()
        books_json = AuthorsBookSerializer(books, many=True)
        books_string = json.dumps(books_json.data)
        books_string = (', '.join(i for i in books_string if i.isdigit()))
        return Response({'id': author.id, 'slug': author.slug, 'author': author.name, 'age': author.age, 'books': books_string})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    lookup_field = "slug"
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        try:
            slug = slugify(request.data.get("title"))
            Book.objects.get(slug=slug)
            return Response("exists", status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def author_age(self, request, slug=None):
        book = self.get_object()
        author = Author.objects.get(id=book.author.id)
        if author.age >= 33:
            book_json = BookAuthorAgeSerializer(book)
            return Response(book_json.data)
        else:
            return Response({'request': 'exist'})
