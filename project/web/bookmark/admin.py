# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Bookmark, BookmarkAdmin)


