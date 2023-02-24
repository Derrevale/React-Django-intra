from blog.models import Category, Article
from django.contrib import admin
# Inscription de la classe CategoryAdmin en tant que gestionnaire de modèle pour la classe Category dans l'interface d'administration de Django
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Affichage de la liste des catégories dans l'interface d'administration avec uniquement le nom de la catégorie
    list_display = ('name',)
    # Pré-remplissage du champ "slug" avec le nom de la catégorie lors de la création d'une nouvelle catégorie dans l'interface d'administration
    prepopulated_fields = {'slug': ('name',)}

# Inscription de la classe ArticleAdmin en tant que gestionnaire de modèle pour la classe Article dans l'interface d'administration de Django
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
