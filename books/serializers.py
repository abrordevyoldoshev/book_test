from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'subtitle', 'author', 'content', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        # title harifga tekshirish uchun yozilgan code
        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': "Title alfabet hariflardan tashkil topgan bolishi kerak"
            })
        if Books.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Title va Author bir xil bo'lmasligi kerak"
                }
            )
        return data

    def validate_price(self,price):

        if price < 0 or price > 999999:

            raise ValidationError(
                {
                    'status': False,
                    'message': "Title va Author bir xil bo'lmasligi kerak"
                }
            )

