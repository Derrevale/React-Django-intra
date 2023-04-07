from django.db import models
from django.dispatch import receiver


class Category_Galerie(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='subcategories')
    image = models.ImageField(upload_to='images/galerie/', null=True, blank=True)
    illustration_image = models.OneToOneField('Image_Galerie', on_delete=models.SET_NULL, null=True, blank=True,
                                              related_name='illustration_for_category')

    def __str__(self):
        return self.title

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Catégorie'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Catégories'


class Image_Galerie(models.Model):
    category = models.ForeignKey(Category_Galerie, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/galerie/')

    def __str__(self):
        return self.image.name

    class Meta:
        # Nom humain de la classe pour l'interface d'administration de Django
        verbose_name = 'Image'
        # Nom humain du pluriel de la classe pour l'interface d'administration de Django
        verbose_name_plural = 'Images'


@receiver(models.signals.pre_delete, sender=Category_Galerie)
def delete_category_files(sender, instance, **kwargs):
    """
    Supprime les fichiers d'images correspondants du dossier de stockage associé lorsque l'instance de l'objet Category est supprimée.
    """
    if instance.image:
        instance.image.delete(False)

    if instance.illustration_image:
        instance.illustration_image.delete(False)


@receiver(models.signals.pre_save, sender=Category_Galerie)
def delete_category_illustration_file(sender, instance, **kwargs):
    """
    Supprime le fichier d'illustration de la catégorie associée lorsque la catégorie est modifiée.
    """
    if instance.pk:
        try:
            old_category = Category_Galerie.objects.get(pk=instance.pk)
        except Category_Galerie.DoesNotExist:
            return

        if old_category.illustration_image and old_category.illustration_image != instance.illustration_image:
            old_category.illustration_image.delete(False)
