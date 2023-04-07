from rest_framework import generics, viewsets
from .models import Category_Galerie, Image_Galerie
from .serializers import Category_GalerieSerializer, Image_GalerieSerializer


class Category_Galerie_ListView(generics.ListCreateAPIView):
    queryset = Category_Galerie.objects.all()
    serializer_class = Category_GalerieSerializer
    tags = ['Galerie - Category']


class Category_Galerie_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category_Galerie.objects.all()
    serializer_class = Category_GalerieSerializer
    tags = ['Galerie - Category']


class Image_Galerie_ListView(generics.ListCreateAPIView):
    queryset = Image_Galerie.objects.all()
    serializer_class = Image_GalerieSerializer
    tags = ['Galerie - Image']


class Image_Galerie_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image_Galerie.objects.all()
    serializer_class = Image_GalerieSerializer
    tags = ['Galerie - Image']


class Category_Galerie_ViewSet(viewsets.ModelViewSet):
    queryset = Category_Galerie.objects.all()
    serializer_class = Category_GalerieSerializer
    tags = ['Galerie - Category']


class Image_Galerie_ViewSet(viewsets.ModelViewSet):
    queryset = Image_Galerie.objects.all()
    serializer_class = Image_GalerieSerializer
    tags = ['Galerie - Image']
