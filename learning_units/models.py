from django.db import models
from programmes.models import Programmes

# Create your models here.
class LearningUnits(models.Model):
    learning_unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    unit_code = models.CharField(max_length=200, unique=True)
    programme_id = models.ForeignKey(
        Programmes,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.unit_name