from django.contrib import admin
from .models import Author, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nick', 'email')
    search_fields = ('nick', 'email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')
    list_filter = ('author',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
# Register your models here.
