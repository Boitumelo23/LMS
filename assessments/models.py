from django.db import models


class Assessment(models.Model):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    facilitator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateTimeField()
    assessment_type = models.CharField(
        max_length=50,
        choices=[
            ('classtest', 'Class Test'),
            ('assignment', 'Assignment'),
            ('exam', 'Exam'),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
