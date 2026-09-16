from django.db import models

# Create your models here.
class Feedback(models.Model):

    feedback_id = models.AutoField(primary_key=True)
    learner_id = models.ForeignKey('learners.Learners', on_delete=models.CASCADE)
    facilitator_id = models.ForeignKey('facilitators.Facilitators', on_delete=models.CASCADE)
    feedback_date = models.DateField()
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback {self.feedback_id} for Learner {self.learner_id}"