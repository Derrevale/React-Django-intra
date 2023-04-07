from django.contrib import admin
from .models import Category_FileManager, Document

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('parent',)
    search_fields = ('name',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)

admin.site.register(Category_FileManager, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
