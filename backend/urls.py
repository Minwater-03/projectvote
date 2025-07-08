from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

# Swagger 스키마 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Project Voting API",
      default_version='v1',
      description="프로젝트 평가 및 투표 API 문서",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('voting.urls')),    # API 경로
    path('', include('voting.urls')),     # 템플릿 경로
    
    # Swagger 문서 URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
