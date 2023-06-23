import os
import random

from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify

from blog import service
from intranet_core.settings import logger


class Languages(models.TextChoices):
    """
    Classe qui représente les langues disponibles pour les articles de blog
    """
    FR = 'fr', 'French'
    NL = 'nl', 'Nederlands'


def _check_category_translations(root_category):
    """
    Check is the category has translations in all the languages supported by the system.
    """

    try:
        categories = list(CategoryBlog.objects.filter(root_category=root_category))
    except Exception as e:
        logger.warning(f'Error while retrieving the categories: {e}')
        categories = []

    if len(categories) < 2:
        translations = service.TranslationService().translate(root_category.name)
        for translation in translations:
            if translation.language not in [category.language for category in categories]:
                category = CategoryBlog(root_category=root_category, name=translation.text,
                                        slug=f'{translation.language}-{root_category.slug}',
                                        language=translation.language)
                try:
                    category.save()
                except Exception as e:
                    logger.warning(f'Error while saving the category: {e}')


class RootCategoryBlog(models.Model):
    """
    Root category entity for blog articles
    """

    name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Name')
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        _check_category_translations(self)

    class Meta:
        verbose_name = 'Root category'
        verbose_name_plural = 'Root categories'


# Classe qui représente une catégorie d'articles de blog dans la base de données
class CategoryBlog(models.Model):
    """
    Category entity for blog articles
    """

    # La catégorie mère
    root_category = models.ForeignKey(RootCategoryBlog, on_delete=models.CASCADE, null=True, blank=False,
                                      verbose_name='Root category')
    # Nom de la catégorie
    name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Name')
    # Champ "slug" généré à partir du nom de la catégorie qui sera utilisé dans les URL
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name='Slug')
    # Langue de la catégorie
    language = models.CharField(max_length=2, choices=Languages.choices, default=Languages.FR, verbose_name='Language')

    # Méthode qui définit comment la catégorie sera affichée dans l'interface d'administration de Django et dans les autres parties de l'application
    def __str__(self):
        return self.name

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Category'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Categories'


def _check_article_translations(root_article):
    """
    Check is the article has title_translations in all the languages supported by the system.
    """

    try:
        articles = list(ArticleBlog.objects.filter(root_article=root_article))
    except Exception as e:
        logger.warning(f'Error while retrieving the articles: {e}')
        articles = []

    if len(articles) < 2:
        translation_service = service.TranslationService()
        title_translations = translation_service.translations_as_dict(translation_service.translate(root_article.title))
        intro_translations = translation_service.translations_as_dict(translation_service.translate(root_article.intro))
        content_translations = translation_service.translations_as_dict(
            translation_service.translate(root_article.content))

        for lang in ('fr', 'nl'):

            if lang not in [article.language for article in articles]:
                category = CategoryBlog.objects.filter(root_category=root_article.category, language=lang).first()
                article = ArticleBlog(root_article=root_article, title=title_translations.get(lang),
                                      intro=intro_translations.get(lang),
                                      content=content_translations.get(lang),
                                      slug=f'{lang}-{root_article.slug}',
                                      language=lang, category=category,
                                      publication_time=root_article.publication_time)
                try:
                    article.save()
                except Exception as e:
                    logger.warning(f'Error while saving the article: {e}')


class RootArticleBlog(models.Model):
    # Titre de l'article
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name='Title')
    slug = models.SlugField(null=True, blank=False, unique=True, verbose_name='Slug')
    # Image d'en-tête de l'article
    header_image = models.ImageField(null=True, blank=True, upload_to="images/blog/")
    # Catégorie à laquelle appartient l'article
    category = models.ForeignKey(RootCategoryBlog, null=True, blank=False, on_delete=models.SET_NULL)
    # Introduction de l'article, utilisant le champ de texte riche de CKEditor
    intro = RichTextField(null=True)
    # Contenu de l'article, utilisant le champ de texte riche de CKEditor
    content = RichTextField(null=True)
    # Heure de publication de l'article
    publication_time = models.DateTimeField(null=False)
    with_translations = models.BooleanField(default=True, verbose_name='With translations')
    language = models.CharField(null=True, blank=True, max_length=2, choices=Languages.choices, default=Languages.FR,
                                verbose_name='Language')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = f'{slugify(self.title)}-{"%06d" % random.randint(100000, 1000000)}'
        super().save(force_insert, force_update, using, update_fields)
        if self.with_translations:
            _check_article_translations(self)

    class Meta:
        verbose_name = 'Root article'
        verbose_name_plural = 'Root articles'


# Classe qui représente un article de blog dans la base de données
class ArticleBlog(models.Model):
    root_article = models.ForeignKey(RootArticleBlog, on_delete=models.CASCADE, null=True, blank=False,
                                     verbose_name='Root article')
    # Titre de l'article
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name='Title')
    slug = models.SlugField(null=True, blank=False, unique=True, verbose_name='Slug')
    # Image d'en-tête de l'article
    header_image = models.ImageField(null=True, blank=True, upload_to="images/blog/")
    # Catégorie à laquelle appartient l'article
    category = models.ForeignKey(CategoryBlog, null=True, blank=False, on_delete=models.SET_NULL)
    # Introduction de l'article, utilisant le champ de texte riche de CKEditor
    intro = RichTextField(null=True)
    # Contenu de l'article, utilisant le champ de texte riche de CKEditor
    content = RichTextField(null=True)
    # Heure de publication de l'article
    publication_time = models.DateTimeField(null=False)
    # Langue de l'article
    language = models.CharField(max_length=2, choices=Languages.choices, default=Languages.FR, verbose_name='Language')

    # Méthode qui définit comment l'article sera affiché dans l'interface d'administration de Django et dans les autres parties de l'application
    def __str__(self):
        return self.title

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Article'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Articles'


# Fonction pour gérer le signal pre_delete et supprimer l'image associée à l'article
@receiver(pre_delete, sender=ArticleBlog)
def article_blog_delete(sender, instance, **kwargs):
    # Supprime l'image d'en-tête de l'article s'il y en a une
    if instance.header_image:
        file_path = os.path.join(settings.MEDIA_ROOT, instance.header_image.path)
        if os.path.isfile(file_path):
            os.remove(file_path)
