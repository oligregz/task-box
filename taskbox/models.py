from django.db import models

class Board(models.Model):
  title = models.CharField(max_length=50)
  
class Tasks(models.Model):
  statusList = [
    ("Pending","Pending"),
    ("Doing","Doing"),
    ("Done","Done")
  ]
  
  board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=50)
  description = models.TextField()
  status = models.CharField(max_length=50, choices=statusList)