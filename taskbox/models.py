from django.db import models

# Create your models here.

class Board(models.Model):
  title = models.CharField(max_length=50)
  
class Tasks(models.Model):
  ...
