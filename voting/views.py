from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Vote
from .serializers import ProjectSerializer, VoteSerializer
from django.db.models import Avg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.annotate(avg_score=Avg('vote__score')).order_by('-avg_score')
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class VoteCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['score'],
            properties={
                'score': openapi.Schema(type=openapi.TYPE_INTEGER, description='1~5점 사이의 점수')
            }
        ),
        responses={201: VoteSerializer()}
    )
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        score = request.data.get('score')

        if not score or int(score) not in [1, 2, 3, 4, 5]:
            return Response({'error': '1~5점 사이의 score를 입력하세요.'}, status=400)

        vote = Vote.objects.create(project=project, score=int(score))
        serializer = VoteSerializer(vote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 템플릿용 뷰

def project_list(request):
    projects = Project.objects.annotate(avg_score=Avg('vote__score')).order_by('-avg_score')
    return render(request, 'voting/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        if score in [1, 2, 3, 4, 5]:
            Vote.objects.create(project=project, score=score)
            return redirect('project_detail', pk=pk)
    
    avg_score = project.vote_set.aggregate(avg=Avg('score'))['avg'] or 0
    return render(request, 'voting/project_detail.html', {
        'project': project,
        'avg_score': round(avg_score, 2)
    })
