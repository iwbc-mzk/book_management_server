from collections import OrderedDict
from rest_framework import serializers
from .models import Book, Author, Series, Publisher, Label, Medium


class AuthorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='author-detail', read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Author
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='series-detail', read_only=True)
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),
                                                   write_only=True,
                                                   allow_null=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('author_id', None)
        del validated_data['author_id']

        return Series.objects.create(**validated_data)

    class Meta:
        model = Series
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='publisher-detail', read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Publisher
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='label-detail', read_only=True)
    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(),
                                                      write_only=True,
                                                      allow_null=True)

    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    def create(self, validated_data):
        validated_data['publisher'] = validated_data.get('publisher_id', None)
        del validated_data['publisher_id']

        return Label.objects.create(**validated_data)

    class Meta:
        model = Label
        fields = '__all__'


class MediumSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='medium-detail', read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Medium
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """参考: https://sakataharumi.hatenablog.jp/entry/2018/10/20/010806"""
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),
                                                   write_only=True,
                                                   allow_null=True)
    series = SeriesSerializer(read_only=True)
    series_id = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all(),
                                                   write_only=True,
                                                   allow_null=True)
    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(),
                                                      write_only=True,
                                                      allow_null=True)
    label = LabelSerializer(read_only=True)
    label_id = serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(),
                                                  write_only=True,
                                                  allow_null=True)
    medium = MediumSerializer(read_only=True)
    medium_id = serializers.PrimaryKeyRelatedField(queryset=Medium.objects.all(),
                                                   write_only=True,
                                                   allow_null=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('author_id', None)
        del validated_data['author_id']

        validated_data['series'] = validated_data.get('series_id', None)
        del validated_data['series_id']

        validated_data['publisher'] = validated_data.get('publisher_id', None)
        del validated_data['publisher_id']

        validated_data['label'] = validated_data.get('label_id', None)
        del validated_data['label_id']

        validated_data['medium'] = validated_data.get('medium_id', None)
        del validated_data['medium_id']

        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = '__all__'






