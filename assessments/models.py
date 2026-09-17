from django.db import models
from learners.models import Learners
from facilitators import models

# Create your models here.
class Assessment(models.Model):

    ASSESSMENT_TYPE =[('Formative', 'Formative'), ('Summative', 'Summative'), ('Final POE', 'Final POE')]

    assessment_id = models.AutoField(primary_key=True)
    assessment_name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPE)
    learning_unit_id = models.ForeignKey('learning_units.LearningUnits', on_delete=models.CASCADE)
    facilitator = models.ForeignKey(models.Facilitators, on_delete=models.CASCADE)

    def __str__(self):
        return self.assessment_name
