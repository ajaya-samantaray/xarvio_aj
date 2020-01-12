import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import BookRating,Book,BookReader,RentBooks
from .serializers import BookRatingSerializer,BookReaderSerializer,RentBooksSerializer


class BookStoreTestCase(APITestCase):
    def test_BookRating(self):
        data={"Rating":6,"Desc":"Extra Ordinary, used for testing only"}
        response = self.client.post("bookrating/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_Books(self):
        data={"ISBN": "978-310-198-1", "TitleName": "My Fifth Book", "AuthorName": "Mr. Ram Samantaray","Rating": 5}
        response = self.client.post("books/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_RentBook(self):
        data={"Book": 1, "Reader": 2, "BorrowDate": "2019-01-01"}
        response = self.client.post("rentbook//",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_BookReader(self):
        data={"Name": "Mr. Sunil Samanta", "Address": "Belgium", "RegistrationDate": "2010-01-01", "IsActive": "Y", "ValidFrom": "2010-01-01", "ValidDate": "2030-12-31"}
        response = self.client.post("reader/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
