from django.db import models

# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length = 200)

class Project(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 50)
    description = models.TextField()
    start_time = models.DateField()
    completion_time = models.DateField()
    total_budget = models.IntegerField()
    completion_percentage = models.FloatField()
    affiliated_agencies = models.ManyToManyField(Agency)

class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

class Issue(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    description = models.TextField()
    sender = models.CharField(max_length = 200)   # TODO make user?