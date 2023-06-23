from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import blog
import documents.views
import import_ad.views
from blog.views import ArticlesViewSet
from blog.views import CategoriesViewSet
from calendrier.views import CalendarysViewset
from calendrier.views import EventViewset
from documents.views import CategoryDocumentViewSet
from documents.views import DocumentViewSet
from galerie.views import Category_Galerie_ViewSet, \
    Image_Galerie_ViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Intranet-Silva-Medical API",
        default_version='v1',
        description="Api de l'Intranet Silva-Medical, "
                    "Cette API permet de gérer les données de l'intranet, "
                    "<br> Elle permet de gérer les données des applications suivantes : "
                    "<ul>"
                    "<li>Calendrier d'événement ( calendrier et événement )</li>"
                    "<li> Gestionnaire de fichier ( catégorie et fichier )</li>"
                    "<li> Galerie d' images ( catégorie et image )</li>"
                    "<li> Blog ( catégorie et article )</li>"
                    "<li> Outils de recherche ( documents )</li>"
                    "</ul>",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register('blog/categories', CategoriesViewSet)
router.register('blog/articles', ArticlesViewSet)

router.register('event/calendar', CalendarysViewset)
router.register('event/events', EventViewset)

router.register('file/categories', CategoryDocumentViewSet)
router.register('file/files', DocumentViewSet)

router.register('gallery/categories', Category_Galerie_ViewSet)
router.register('gallery/images', Image_Galerie_ViewSet)

urlpatterns = [
                  # Authentication
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  # Administration
                  path('admin/', admin.site.urls),
                  # API
                  path('api/', include(router.urls)),

                  # Media
                  path('images/<str:path>', serve, {'document_root': settings.MEDIA_ROOT}),

                  # Search documents
                  path('api/documents/search/', documents.views.SearchView.as_view(), name='search'),

                  # Search blog
                  path('api/blog/search/', blog.views.SearchBlogView.as_view(), name='search_blog'),

                  # Import from Active Directory
                  path('api/users/import/', import_ad.views.ActiveDirectoryView.as_view(), name='ad_import'),
                  # Search users
                  path('api/users/search/', import_ad.views.SearchUserView.as_view(), name='search_user'),

                  # Documentation
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
