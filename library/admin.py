from django.contrib import admin


# Register your models here.
from .models import Book, Member

admin.site.register(Book)
admin.site.register(Member)

