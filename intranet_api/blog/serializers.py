from .models import Category_Blog
from .models import Article_Blog

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Blog
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Blog
        fields = '__all__'
