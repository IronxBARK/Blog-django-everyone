from django.contrib import admin
from .models import BlogEntry

# Register your models here.
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author__username')
    list_filter = ('date',)

admin.site.register(BlogEntry, BlogEntryAdmin)