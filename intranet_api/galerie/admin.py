from django.contrib import admin
from .models import Category_Galerie, Image_Galerie

class ImageInline(admin.TabularInline):
    model = Image_Galerie

class Category_GalerieAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    def parent_category_name(self, obj):
        return obj.parent_category.name if obj.parent_category else 'N/A'
    parent_category_name.short_description = 'Catégorie parente'

    list_display = ('name', 'parent_category_name', 'image', 'illustration_image')
    search_fields = ('name',)
    list_filter = ('parent_category',)

class Image_GalerieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image')
    search_fields = ('name', 'category__name',)
    list_filter = ('category',)
    readonly_fields = ('name',)

admin.site.register(Category_Galerie, Category_GalerieAdmin)
admin.site.register(Image_Galerie, Image_GalerieAdmin)
