from django.db import models
from learners.models import Learners
from facilitators import models

# Create your models here.
class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    assessment_name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    submission_date = models.DateField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.DecimalField(max_digits=5, decimal_places=2)
    result_status = models.CharField(max_length=10, choices=[('Pass', 'Pass'), ('Fail', 'Fail')])
    assessment_type = models.CharField(max_length=20, choices=[('Formative', 'Formative'), ('Summative', 'Summative'), ('Final POE', 'Final POE')])
    submission_status = models.CharField(max_length=20, choices=[('Submitted', 'Submitted'), ('Not Submitted', 'Not Submitted')])
    learner_id = models.ManyToManyField(Learners, related_name='assessments')
    learning_unit_id = models.ForeignKey('learning_units.LearningUnits', on_delete=models.CASCADE)
    facilitator = models.ForeignKey(models.Facilitators, on_delete=models.CASCADE)

    def __str__(self):
        return self.assessment_name
