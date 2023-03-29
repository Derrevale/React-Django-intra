from django.db import models
import os


def get_upload_path(instance, filename):
    return os.path.join('images', 'documents', filename)


class Category(models.Model):
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
    categories = models.ManyToManyField(Category, related_name='documents')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = os.path.basename(self.fileUrl.name)
        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
