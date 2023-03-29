from rest_framework import serializers
from .models import Category, Document


class CategoryDocumentSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)
    files = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children', 'files')
        depth = 1

    def get_files(self, category):
        """
        Returns a list of files associated with this category
        """
        document_serializer = DocumentSerializer(instance=category.documents.all(), many=True)
        return document_serializer.data


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'name', 'description', 'fileUrl', 'categories')
