from django.contrib import admin
from .models import Book, Publisher, Category, Review

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Review)
# Register your models here.
