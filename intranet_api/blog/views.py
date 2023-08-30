from rest_framework import views, status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import ArticleBlog, RootArticleBlog, RootCategoryBlog
from .models import CategoryBlog
from .serializers import ArticleSerializer
from .serializers import CategorySerializer


# Create a custom pagination class for blog articlesŒ
class BlogArticlePagination(PageNumberPagination):
    page_size = 12  # Or any number you prefer


class CategoryBlogListAPIView(views.APIView):
    """
    CategoryBlog API View.
    """

    @staticmethod
    def get(request):
        """
        Handles GET requests.
        :param request: the request.
        """

        # Get all the documents
        categories = CategoryBlog.objects.all()
        # Serialize the documents
        serialized_categories = CategorySerializer(categories, many=True).data

        return Response(serialized_categories)

    @staticmethod
    def post(request):
        """
        Handles POST requests.
        :param request: the request.
        """

        # Create a new document from the JSON request
        category = RootCategoryBlog(name=request.data.get('name'), slug=request.data.get('slug'))
        category.save()

        categories = CategoryBlog.objects.filter(root_category=category).all()
        # Serialize the document
        serialized_categories = CategorySerializer(categories, many=True).data

        return Response(serialized_categories)


class CategoryBlogDetailsAPIView(views.APIView):

    @staticmethod
    def get(request, cat_id: int):
        """
        Handles GET requests.
        """

        # Get the document
        category = get_object_or_404(CategoryBlog, pk=cat_id)
        # Serialize the document
        serialized_category = CategorySerializer(category).data

        return Response(serialized_category)

    @staticmethod
    def put(request, cat_id: int):
        """
        Handles PUT requests.
        """
        category = get_object_or_404(CategoryBlog, pk=cat_id)
        category.name = request.data.get('name')
        category.slug = request.data.get('slug')
        category.language = request.data.get('language')
        category.save()

        serialized_category = CategorySerializer(category).data

        return Response(serialized_category)


class ArticlesBlogListAPIView(views.APIView):
    """
    ArticleBlog API View.
    """
    pagination_class = BlogArticlePagination

    @staticmethod
    def get(request):
        """
        Handles GET requests.
        :param request: the request.
        """

        # Get all the documents
        articles = ArticleBlog.objects.all()
        art_ids = [art.root_article.id for art in articles]
        _root_articles = RootArticleBlog.objects.all()
        root_articles = [art for art in _root_articles if art.id not in art_ids]

        # Combine the articles
        combined_articles = list(articles) + list(root_articles)

        # Apply pagination
        paginator = BlogArticlePagination()
        paginated_articles = paginator.paginate_queryset(combined_articles, request)

        # Serialize the documents
        serialized_articles = ArticleSerializer(paginated_articles, many=True).data

        return paginator.get_paginated_response(serialized_articles)


class ArticlesBlogDetailsAPIView(views.APIView):
    """
    ArticleBlog API View.
    """

    @staticmethod
    def get(request, slug: str):
        """
        Handles GET requests.
        :param request: the request.
        :param slug: the slug of the article.
        """

        try:
            article = ArticleBlog.objects.filter(slug=slug).first()
        except ArticleBlog.DoesNotExist:
            article = None

        article = get_object_or_404(RootArticleBlog, slug=slug)

        # Serialize the documents
        serialized_article = ArticleSerializer(article).data

        return Response(serialized_article)


class SearchBlogView(views.APIView):
    """
    Search blog articles.
    """

    QUERY_PARAM = 'q'

    def __init__(self):
        """
        Constructor.
        """

        # Call the parent constructor.
        super().__init__()
        # Set the serializer class.
        self.serializer_class = ArticleSerializer

    def get(self, request):
        """
        Handles GET requests.
        :param request: the request.
        """

        if self.QUERY_PARAM not in request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Search on the documents
        articles = ArticleBlog.objects.filter(content__icontains=request.GET.get(self.QUERY_PARAM))
        art_ids = [art.root_article.id for art in articles]
        _root_articles = RootArticleBlog.objects.filter(content__icontains=request.GET.get(self.QUERY_PARAM))
        root_articles = [art for art in _root_articles if art.id not in art_ids]
        # Serialize the found documents
        serialized_articles = self.serializer_class(articles, many=True).data
        serialized_articles += self.serializer_class(root_articles, many=True).data

        return Response(serialized_articles)
