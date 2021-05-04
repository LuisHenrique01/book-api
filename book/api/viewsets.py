from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from book.models import Book, Author, PublishingCompany
from book.api.serializers import BookSerializer, AuthorSerializer, PublishingCompanySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['isbn', 'author', 'publishing_company']
    search_fields = ['title']
    ordering = ['title']



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering = ['name']


class PublishingCompanyViewSet(ModelViewSet):
    queryset = PublishingCompany.objects.all()
    serializer_class = PublishingCompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering = ['name']