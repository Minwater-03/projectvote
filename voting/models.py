from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_score(self):
        scores = self.vote_set.all().values_list('score', flat=True)
        return round(sum(scores) / len(scores), 2) if scores else 0

    def __str__(self):
        return self.title


class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()  # 1~5점
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.score}점"