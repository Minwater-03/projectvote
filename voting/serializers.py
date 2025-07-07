from rest_framework import serializers
from .models import Project, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'score', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    average_score = serializers.FloatField(source='avg_score', read_only=True) 

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'github_url', 'created_at', 'average_score']