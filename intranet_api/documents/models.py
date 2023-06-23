import os

from django.db import models
from django.dispatch import receiver

from intranet_core.settings import logger


def get_upload_path(instance, filename):
    return os.path.join('images', 'documents', filename)


class Category_FileManager(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        if self.parent:
            return f'{self.parent} > {self.name}'
        return self.name

    def documents(self):
        """
        Returns a queryset of documents associated with this category
        """
        return self.documents.all()


class Document(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    fileUrl = models.FileField(upload_to=get_upload_path)
    categories = models.ManyToManyField(Category_FileManager, related_name='documents')
    processed = models.BooleanField(default=False)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f"Document {self.id}"

    def save(self, *args, **kwargs):
        """
        Saves the document and launches the process if needed.
        """

        # Performs the save
        super().save(*args, **kwargs)

        # Checks if the document needs to be processed
        if not self.processed:
            try:
                import documents.services as services
                # If so, process it
                services.silva_search_service.process(self)
                # Mark it as processed
                self.processed = True
                # Save it
                super().save(*args, **kwargs)
            except Exception as e:
                logger.error(f'Error while processing document {self.name}: {e}')

    def get_filename(self):
        """
        Returns the filename of the document.
        :return: the filename of the document.
        """
        return os.path.basename(self.fileUrl.name)


@receiver(models.signals.pre_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `Document` object is deleted.
    """
    if instance.fileUrl:
        if os.path.isfile(instance.fileUrl.path):
            os.remove(instance.fileUrl.path)


@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem when corresponding `Document` object is updated
    with new file.
    """
    if not instance.id:
        return False

    try:
        old_file = Document.objects.get(pk=instance.id).fileUrl
    except Document.DoesNotExist:
        return False

    new_file = instance.fileUrl
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
