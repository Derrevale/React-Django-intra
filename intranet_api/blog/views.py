from rest_framework import viewsets, views, status
from rest_framework.decorators import action
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


class CategoryBlogAPIView(views.APIView):
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


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryBlog.objects.all()
    tags = ['Blog - Category']

    @action(methods=['post'], detail=True)
    def do_create(self, request, *args, **kwargs):
        print(request)
        pass

    @action(methods=['put'], detail=True)
    def do_update(self, request, *args, **kwargs):
        print(request)
        pass


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = ArticleBlog.objects.all()
    pagination_class = BlogArticlePagination  # Add this line
    tags = ['Blog - Article']

    @action(methods=['post'], detail=True)
    def do_create(self, request, *args, **kwargs):
        pass

    @action(methods=['put'], detail=True)
    def do_update(self, request, *args, **kwargs):
        pass


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
        root_articles = RootArticleBlog.objects.filter(content__icontains=request.GET.get(self.QUERY_PARAM))
        # Serialize the found documents
        serialized_articles = self.serializer_class(articles, many=True).data

        return Response(serialized_articles)
