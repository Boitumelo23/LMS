from django.db import models

# Create your models here.
class Facilitators(models.Model):
    facilitator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=50, choices=[('Facilitator', 'Facilitator'), ('Mentor', 'Mentor')])

    def __str__(self):
        return self.facilitator_name