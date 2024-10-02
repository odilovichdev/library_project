from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from book.models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = 'id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price'

    def validate(self, attrs):
        author = attrs.get('author', None)
        isbn = attrs.get('isbn', None)

        if Book.objects.filter(author=author, isbn=isbn).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bu foydalanuvchi allaqachon mavjud"
                }
            )

        return attrs

    def validate_price(self, attrs):
        print(type(attrs))
        if attrs < 0 and attrs < 999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx xato kiritildi"
                }
            )
        return attrs
