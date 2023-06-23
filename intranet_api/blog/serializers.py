from rest_framework import serializers

from .models import ArticleBlog


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    slug = serializers.SlugField(max_length=50)
    language = serializers.CharField(max_length=2)


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = ArticleBlog
        fields = '__all__'
