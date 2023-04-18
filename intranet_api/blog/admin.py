from blog.models import Category_Blog, Article_Blog
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Afficher le nom et le slug dans la liste des catégories
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)  # Ajouter une barre de recherche pour trouver facilement une catégorie
    ordering = ('name',)  # Trier les catégories par ordre alphabétique
    list_per_page = 20  # Afficher 20 catégories par page


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_time')  # Afficher le titre, la catégorie et la date de publication dans la liste des articles
    list_editable = ('category',)  # Permettre la modification de la catégorie directement dans la liste des articles
    search_fields = ('title', 'category__name')  # Ajouter une barre de recherche pour trouver facilement un article par titre ou catégorie
    list_filter = ('category',)  # Ajouter des filtres pour filtrer les articles par catégorie
    ordering = ('-publication_time',)  # Trier les articles par date de publication, en ordre décroissant
    list_per_page = 20  # Afficher 20 articles par page


admin.site.register(Category_Blog, CategoryAdmin)
admin.site.register(Article_Blog, ArticleAdmin)
