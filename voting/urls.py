from django.urls import path
from .views import (
    ProjectListAPIView, ProjectDetailAPIView, VoteCreateAPIView,
    project_list, project_detail  # 템플릿용 view도 import!
)

urlpatterns = [
    # API 뷰
    path('api/projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('api/projects/<int:pk>/vote/', VoteCreateAPIView.as_view(), name='project-vote'),

    # HTML 템플릿 뷰
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
]
