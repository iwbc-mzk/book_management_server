from collections import OrderedDict
from rest_framework import serializers
from .models import Book, Author, Series, Publisher, Label, Medium
import json


class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)

        return str(self.get_queryset().get(pk=value.pk))


class AuthorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Author
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    author = MyPrimaryKeyRelatedField(queryset=Author.objects.all())

    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Series
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Publisher
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    publisher = MyPrimaryKeyRelatedField(queryset=Publisher.objects.all())

    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Label
        fields = '__all__'


class MediumSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Medium
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = MyPrimaryKeyRelatedField(queryset=Author.objects.all())
    series = MyPrimaryKeyRelatedField(queryset=Series.objects.all())
    publisher = MyPrimaryKeyRelatedField(queryset=Publisher.objects.all())
    label = MyPrimaryKeyRelatedField(queryset=Label.objects.all())
    medium = MyPrimaryKeyRelatedField(queryset=Medium.objects.all())

    author_url = serializers.HyperlinkedRelatedField(source='author', view_name='author-detail', read_only=True)
    series_url = serializers.HyperlinkedRelatedField(source='series', view_name='series-detail', read_only=True)
    publisher_url = serializers.HyperlinkedRelatedField(source='publisher',
                                                        view_name='publisher-detail',
                                                        read_only=True)
    label_url = serializers.HyperlinkedRelatedField(source='label', view_name='label-detail', read_only=True)
    medium_url = serializers.HyperlinkedRelatedField(source='medium', view_name='medium-detail', read_only=True)

    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Book
        fields = '__all__'






