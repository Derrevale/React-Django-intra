from django.contrib import admin

from blog.models import CategoryBlog, ArticleBlog, RootCategoryBlog, RootArticleBlog


class RootCategoryAdmin(admin.ModelAdmin):
    # Afficher le nom et le slug dans la liste des catégories
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    # Ajouter une barre de recherche pour trouver facilement une catégorie
    search_fields = ('name',)
    # Trier les catégories par ordre alphabétique
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    # Afficher le nom et le slug dans la liste des catégories
    list_display = ('root_category', 'name', 'language', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    # Ajouter des filtres pour filtrer les catégories par langue
    list_filter = ('root_category', 'language',)
    # Ajouter une barre de recherche pour trouver facilement une catégorie
    search_fields = ('root_category', 'language', 'name',)
    # Trier les catégories par ordre alphabétique
    ordering = ('root_category', 'name',)
    # Afficher 20 catégories par page
    list_per_page = 20


class RootArticleAdmin(admin.ModelAdmin):
    # Afficher le titre, la catégorie et la date de publication dans la liste des articles
    list_display = ('title', 'category', 'publication_time',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('category',)
    search_fields = ('title', 'category__name',)
    list_filter = ('category',)
    ordering = ('-publication_time',)
    # Afficher 20 articles par page
    list_per_page = 20


class ArticleAdmin(admin.ModelAdmin):
    # Afficher le titre, la catégorie et la date de publication dans la liste des articles
    list_display = ('root_article', 'title', 'category', 'language', 'publication_time')
    prepopulated_fields = {'slug': ('title',)}
    # Permettre la modification de la catégorie directement dans la liste des articles
    list_editable = ('category',)
    # Ajouter une barre de recherche pour trouver facilement un article par titre ou catégorie
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'language')
    # Trier les articles par date de publication, en ordre décroissant
    ordering = ('-publication_time',)
    # Afficher 20 articles par page
    list_per_page = 20


admin.site.register(CategoryBlog, CategoryAdmin)
admin.site.register(RootCategoryBlog, RootCategoryAdmin)

admin.site.register(ArticleBlog, ArticleAdmin)
admin.site.register(RootArticleBlog, RootArticleAdmin)
