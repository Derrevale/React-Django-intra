from rest_framework import viewsets
from .models import Category, Document
from .serializers import CategoryDocumentSerializer, DocumentSerializer

class CategoryDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryDocumentSerializer
    queryset = Category.objects.all()

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
