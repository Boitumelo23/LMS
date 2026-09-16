from django.db import models

# Create your models here.
class AssessmentsSubmissions(models.Model):

    SUBMISSION_STATUS= [('Submitted', 'Submitted'), ('Not Submitted', 'Not Submitted')]
    RESULT_STATUSES = [('Pass', 'Pass'), ('Fail', 'Fail')]

    submission_id = models.AutoField(primary_key=True)
    assessment_id = models.ForeignKey('assessments.Assessment', on_delete=models.CASCADE)
    learner_id = models.ForeignKey('learners.Learners', on_delete=models.CASCADE)
    submission_date = models.DateField()
    submission_file = models.FileField(upload_to='submissions/')
    result = models.DecimalField(max_digits=5, decimal_places=2)
    result_status = models.CharField(max_length=10, choices=RESULT_STATUSES, default='Fail')
    submission_status = models.CharField(max_length=20, choices=SUBMISSION_STATUS, default='Not Submitted')
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Submission {self.submission_id} for Assessment {self.assessment_id}"