from django.db import models

# Create your models here.
class PredResults(models.Model):

    age = models.FloatField()
    bmi = models.FloatField()
    glucose = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification