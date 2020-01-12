from django.shortcuts import render
from rest_framework import viewsets
from .models import BookRating, Book,BookReader,RentBooks
from .serializers import BookRatingSerializer, BookSerializer,BookReaderSerializer,RentBooksSerializer
# Create your views here.


class BookRatingView(viewsets.ModelViewSet):
    queryset = BookRating.objects.all()
    serializer_class = BookRatingSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookReaderView(viewsets.ModelViewSet):
    queryset = BookReader.objects.all()
    serializer_class = BookReaderSerializer


class RentBooksView(viewsets.ModelViewSet):
    queryset = RentBooks.objects.all()
    serializer_class = RentBooksSerializer