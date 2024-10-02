from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializers


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
