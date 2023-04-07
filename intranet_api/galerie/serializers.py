from rest_framework import serializers
from .models import Category_Galerie, Image_Galerie


class Category_GalerieSerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category_Galerie
        fields = ['id', 'name', 'parent_category', 'image', 'illustration_image', 'subcategories', 'images']


class Image_GalerieSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category_Galerie.objects.all())

    class Meta:
        model = Image_Galerie
        fields = ['id', 'category', 'image']
