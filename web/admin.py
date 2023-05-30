from django.contrib import admin
from .models import Author, Publisher, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass