from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    context=models.TextField()
    date=models.DateField()
class Cirrhosis(models.Model):
    drug=models.IntegerField()
    ascites=models.IntegerField()
    hepatomegaly=models.IntegerField()
    spiders=models.IntegerField()
    edema=models.IntegerField()
    bilirubin=models.FloatField()
    cholesterol=models.FloatField()
    albumin=models.FloatField()
    copper=models.FloatField()
    alk_phos=models.FloatField()
    sgot=models.FloatField()
    triglycerides=models.FloatField()
    platelets=models.FloatField()
    prothrombin=models.FloatField()