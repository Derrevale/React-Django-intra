from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    slug = serializers.SlugField(max_length=50)


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    slug = serializers.SlugField(max_length=150)
    header_image = serializers.ImageField()
    category = CategorySerializer()
    intro = serializers.CharField()
    content = serializers.CharField()
    publication_time = serializers.DateTimeField()
    language = serializers.CharField(max_length=2)
