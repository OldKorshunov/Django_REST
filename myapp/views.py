from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Author, Book
from serializers import AuthorSerializer, BookSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, ViewSet


# @api_view(["GET", "POST"])
# def sample_app(request: Request) -> Response:
#     if request.method == "GET":
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)





