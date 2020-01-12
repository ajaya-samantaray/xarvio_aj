from django.db import models
import datetime
# Create your models here.


class BookRating(models.Model):
    RatingID = models.IntegerField(primary_key=True)
    Desc = models.CharField(max_length=100)

    class Meta:
        ordering = ['RatingID']
    def __str__(self):
        return str(self.RatingID)

class Book(models.Model):
    ISBN = models.CharField('ISBN', max_length=13, help_text='13 Character <a href = "https://www.isbn-international.org/content/what-isbn">ISBN Number</a>')
    TitleName = models.CharField(max_length=100)
    AuthorName=models.CharField(max_length=100)
    Rating = models.ForeignKey(BookRating, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id', 'ISBN']
        ordering = ['TitleName']

    def __str__(self):
        return self.TitleName


class BookReader(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    RegistrationDate = models.DateField()
    IsActive = models.CharField(max_length=1)
    ValidFrom = models.DateField(default=datetime.date.today)
    ValidDate = models.DateField()

    def __str__(self):
        return self.Name


class RentBooks(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Reader = models.ForeignKey(BookReader, on_delete=models.CASCADE)
    BorrowDate = models.DateField(null=True,blank=True)
    ReturnDate = models.DateField(null=True, blank=True)
