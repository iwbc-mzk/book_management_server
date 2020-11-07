from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer


# Create your views here.
class ListBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
