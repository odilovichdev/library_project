from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = 'title', 'subtitle', 'author', 'isbn', 'price'
    list_filter = 'title', 'author', 'price'
    search_fields = 'title', 'author', 'price'
