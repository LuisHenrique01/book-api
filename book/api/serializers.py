from rest_framework import serializers
from book.models import Book, Author, PublishingCompany


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublishingCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = PublishingCompany
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'