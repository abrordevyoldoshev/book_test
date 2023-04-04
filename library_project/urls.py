from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book list Api",
        default_version="v1",
        description="Library demo project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email='frontend47@gmail.com'),
        license=openapi.License(name='Demo license')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

urlpatterns = [
    # Custom code
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    # rest_framework online
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj_rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj_rest_auth/register/', include('dj_rest_auth.registration.urls')),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
