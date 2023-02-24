from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from blog.views import CategorysViewset
from blog.views import ArticlesViewset

from calendrier.views import CalendarysViewset
from calendrier.views import EventViewset

schema_view = get_schema_view(
    openapi.Info(
        title="Intranet-Silva-Medical API",
        default_version='v1',
        description="Api de l'application Rolisticae, "
                    "<br> Catégorie de blog"
                    "<br> Article de blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register('category', CategorysViewset)
router.register('article', ArticlesViewset)

router.register('calendrier', CalendarysViewset)
router.register('event', EventViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('images/<str:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
