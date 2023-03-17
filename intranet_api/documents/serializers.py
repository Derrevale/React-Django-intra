from rest_framework import serializers
from .models import Category, Document

class CategoryDocumentSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children')

class DocumentSerializer(serializers.ModelSerializer):
    categories = CategoryDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'name', 'description', 'file', 'categories')
