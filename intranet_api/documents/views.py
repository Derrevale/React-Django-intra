from rest_framework import viewsets, views, status
from rest_framework.response import Response

from .models import Category_FileManager, Document
from .serializers import CategoryDocumentSerializer, DocumentSerializer


class CategoryDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryDocumentSerializer
    queryset = Category_FileManager.objects.all()
    tags = ['FileManager - Category']


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    tags = ['FileManager - File']


class SearchView(views.APIView):
    """
    Search documents.
    """

    QUERY_PARAM = 'q'

    def __init__(self):
        """
        Constructor.
        """

        # Call the parent constructor.
        super().__init__()
        # Set the serializer class.
        self.serializer_class = DocumentSerializer

        # Get the search service.
        import documents.services as services
        self.search_service = services.silva_search_service

    def get(self, request):
        """
        Handles GET requests.
        :param request: the request.
        """

        if self.QUERY_PARAM not in request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Search on the documents
        documents = self.search_service.search(request.GET.get(self.QUERY_PARAM))
        # Serialize the found documents
        serialized_documents = self.serializer_class(documents, many=True).data

        return Response(serialized_documents)

