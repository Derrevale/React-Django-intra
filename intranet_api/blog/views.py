from rest_framework import viewsets

from .models import Article_Blog
from .models import Category_Blog
from .serializers import ArticleSerializer
from .serializers import CategorySerializer


# Importez les modèles de catégorie et d'article de blog, ainsi que les sérialiseurs associés.

# Créez une classe CategoriesViewSet qui hérite de viewsets.ModelViewSet.
# Cette classe gère les vues de l'API pour les catégories de blog.
class CategoriesViewSet(viewsets.ModelViewSet):
    # Spécifiez le sérialiseur à utiliser pour traiter les données de catégorie.
    serializer_class = CategorySerializer
    # Définissez le queryset à utiliser pour récupérer les données de catégorie de la base de données.
    queryset = Category_Blog.objects.all()
    # Ajoutez une liste de tags pour faciliter la compréhension et l'organisation de cette vue.
    tags = ['Blog - Category']


# Créez une classe ArticlesViewSet qui hérite de viewsets.ModelViewSet.
# Cette classe gère les vues de l'API pour les articles de blog.
class ArticlesViewSet(viewsets.ModelViewSet):
    # Spécifiez le sérialiseur à utiliser pour traiter les données d'article.
    serializer_class = ArticleSerializer
    # Définissez le queryset à utiliser pour récupérer les données d'article de la base de données.
    queryset = Article_Blog.objects.all()
    # Ajoutez une liste de tags pour faciliter la compréhension et l'organisation de cette vue.
    tags = ['Blog - Article']
