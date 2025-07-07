from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView, VoteCreateAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/<int:pk>/vote/', VoteCreateAPIView.as_view(), name='project-vote'),
]