from django.db import models

# Create your models here.
class Learners(models.Model):
    learner_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    id_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email_address = models.EmailField(unique=True)
    application_date = models.DateField(auto_now_add=True)
    applicaton_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    document_type = models.CharField(max_length=50, choices=[('Affidavit', 'Affidavit'), ('ID', 'ID'), ('CV', 'CV'), ('Matric Certificate', 'Matric Certificate'), ('SARS Document', 'SARS Document')])
    enrollment_date = models.DateField(auto_now_add=True)
   

    def __str__(self):
        return self.first_name + ' ' + self.last_name