from django.db import models

# Create your models here.
class Programmes(models.Model):
    NQF_LEVEL =[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')]

    programme_id = models.AutoField(primary_key=True)
    programme_name = models.CharField(max_length=100)
    programme_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    nqf_level = models.CharField(max_length=10, choices=NQF_LEVEL)
    credits = models.IntegerField()

    def __str__(self):
        return self.programme_name