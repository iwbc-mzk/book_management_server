from collections import OrderedDict
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'created_by', 'created_at',
                  'updated_by', 'updated_at', 'del_flg']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'author_name', 'created_at',
                  'updated_by', 'updated_at', 'del_flg']


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, source='author_id')
    series = serializers.StringRelatedField(read_only=True, source='series_id')
    publisher = serializers.StringRelatedField(read_only=True, source='publisher_id')
    label = serializers.StringRelatedField(read_only=True, source='label_id')

    class Meta:
        model = Book
        fields = ['title', 'author', 'series', 'publisher', 'label',
                  'created_by', 'created_at', 'updated_by', 'updated_at', 'del_flg']
