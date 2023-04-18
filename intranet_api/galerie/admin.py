from django.contrib import admin
from .models import Category_Galerie, Image_Galerie


class ImageInline(admin.TabularInline):
    model = Image_Galerie


class Category_GalerieAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('name', 'parent_category', 'image', 'illustration_image')


class Image_GalerieAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'image')


admin.site.register(Category_Galerie, Category_GalerieAdmin)
admin.site.register(Image_Galerie, Image_GalerieAdmin)
