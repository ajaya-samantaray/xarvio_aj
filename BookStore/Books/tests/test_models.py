import sys,os,datetime
from pathlib import Path
_projectDir = Path(__file__).resolve().parents[1]
sys.path.append(os.path.join(_projectDir))
from django.test import TestCase
from models import BookRating


class BookRatingTest(TestCase):
    """ Test module for BookRating model """

    def setUp(self):
        BookRating.objects.create(
            RatingID=0, Desc='Need improvement. Used for testing')

    def test_BookRating(self):
        bookRating_0 = BookRating.objects.get(RatingID=0)
        assert bookRating_0 == 0