from django.contrib import admin
from .models import Book, Author, Series, Publisher, Label, Medium


# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Publisher)
admin.site.register(Label)
admin.site.register(Medium)
