from django.db import models

# Create your models here.
class Warning(models.Model):

    warning_id = models.AutoField(primary_key=True)
    learner_id = models.ForeignKey('learners.Learners', on_delete=models.CASCADE)
    warning_date = models.DateField()
    warning_reason = models.TextField()

    def __str__(self):
        return f"Warning {self.warning_id} for Learner {self.learner_id}"