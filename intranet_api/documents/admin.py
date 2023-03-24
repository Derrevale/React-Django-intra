from django.contrib import admin
from .models import Category, Document

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('parent',)
    search_fields = ('name',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    exclude = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
