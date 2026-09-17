from django.db import models

# Create your models here.
class Learners(models.Model):

    GENDER = [('Male','Male'), ('Female','Female')]
    APPLICATION_STATUS =[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]

    learner_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    id_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    email_address = models.EmailField(unique=True)
    application_date = models.DateField(auto_now_add=True)
    applicaton_status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='Pending')
    enrollment_date = models.DateField(null = True, blank= True)
    programme_id = models.ForeignKey('programmes.Programmes', on_delete=models.CASCADE, default=1)
    cv_document = models.FileField(upload_to='learner_documents')
    id_document = models.FileField(upload_to='learner_documents')
    sars_document = models.FileField(upload_to='learner_documents')
    matric_document = models.FileField(upload_to='learner_documents')
    affidavit_document = models.FileField(upload_to='learner_documents')


    def __str__(self):
        return self.first_name + ' ' + self.last_name