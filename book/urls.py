from django.urls import path
from rest_framework.routers import SimpleRouter

from book.views import BookListCreateAPIView, \
    BookRetrieveUpdateDestroyAPIView, BookViewSet

router = SimpleRouter()

router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('books-list-create/', BookListCreateAPIView.as_view()),
    path('books-retrieve-update-destroy/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns += router.urls
