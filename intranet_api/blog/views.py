from rest_framework import viewsets, views, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import ArticleBlog
from .models import CategoryBlog
from .serializers import ArticleSerializer
from .serializers import CategorySerializer


# Create a custom pagination class for blog articlesŒ
class BlogArticlePagination(PageNumberPagination):
    page_size = 12  # Or any number you prefer


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
        # Serialize the found documents
        serialized_articles = self.serializer_class(articles, many=True).data

        return Response(serialized_articles)
