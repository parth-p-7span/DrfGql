from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'desc',
        'author',
    ]
