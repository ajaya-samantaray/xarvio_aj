from rest_framework import serializers
from six import string_types
from .models import BookRating,Book,BookReader,RentBooks
from rest_framework.serializers import ValidationError


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class BookRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRating
        fields = ('RatingID','Desc')


class BookSerializer(serializers.ModelSerializer):

    # url = serializers.HyperlinkedIdentityField(
    #     view_name='book-detail',
    #     lookup_field='TitleName'
    # )

    class Meta:
        model = Book
        fields = ('url','ISBN','TitleName','AuthorName','Rating')

    def validate_ISBN(self, value):
        """ Check string is a valid ISBN number"""
        isbn_to_check = value.replace('-', '').replace(' ', '')

        if not isinstance(isbn_to_check, string_types):
            raise ValidationError(u'Invalid ISBN: Not a string')

        if len(isbn_to_check) != 10 and len(isbn_to_check) != 13:
            raise ValidationError(u'Invalid ISBN: Wrong length')

        if isbn_to_check != isbn_to_check.upper():
            raise ValidationError(u'Invalid ISBN: Only upper case allowed')

        return value



class BookReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookReader
        fields = ('url','Name','Address','RegistrationDate','IsActive','ValidFrom','ValidDate')


class RentBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBooks
        fields = ('url','Book','Reader','BorrowDate','ReturnDate')


    def validate(self, data):
        """
        Check that the borrow date is before the return date.
        """
        if data['ReturnDate'] and data['BorrowDate'] > data['ReturnDate']:
            raise serializers.ValidationError("Return must occur after the borrowing")
        return data