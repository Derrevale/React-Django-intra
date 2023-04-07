from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
import os

# Classe qui représente une catégorie d'articles de blog dans la base de données
class Category_Blog(models.Model):
    # Nom de la catégorie
    name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Name')
    # Champ "slug" généré à partir du nom de la catégorie qui sera utilisé dans les URL
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name='Slug')

    # Méthode qui définit comment la catégorie sera affichée dans l'interface d'administration de Django et dans les autres parties de l'application
    def __str__(self):
        return self.name

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Category'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Categories'

# Classe qui représente un article de blog dans la base de données
class Article_Blog(models.Model):
    # Titre de l'article
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name='Title')
    # Image d'en-tête de l'article
    header_image = models.ImageField(null=True, blank=True, upload_to="images/blog/")
    # Catégorie à laquelle appartient l'article
    category = models.ForeignKey(Category_Blog, null=True, blank=False, on_delete=models.SET_NULL)
    # Introduction de l'article, utilisant le champ de texte riche de CKEditor
    intro = RichTextField(null=True)
    # Contenu de l'article, utilisant le champ de texte riche de CKEditor
    content = RichTextField(null=True)
    # Heure de publication de l'article
    publication_time = models.DateTimeField(null=False)

    # Méthode qui définit comment l'article sera affiché dans l'interface d'administration de Django et dans les autres parties de l'application
    def __str__(self):
        return self.title

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Article'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Articles'

# Fonction pour gérer le signal pre_delete et supprimer l'image associée à l'article
@receiver(pre_delete, sender=Article_Blog)
def article_blog_delete(sender, instance, **kwargs):
    # Supprime l'image d'en-tête de l'article s'il y en a une
    if instance.header_image:
        file_path = os.path.join(settings.MEDIA_ROOT, instance.header_image.path)
        if os.path.isfile(file_path):
            os.remove(file_path)
