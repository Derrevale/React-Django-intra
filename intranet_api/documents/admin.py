from django.contrib import admin
from .models import Category_FileManager, Document

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'processed', 'get_filename')
    list_filter = ('processed', 'categories')
    search_fields = ('name', 'description',)

admin.site.register(Category_FileManager, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
