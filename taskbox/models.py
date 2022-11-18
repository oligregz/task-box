from django.db import models

class Board(models.Model):
  title = models.CharField(max_length=50)
  
  def __str__(self):
    return self.title
  
class Task(models.Model):
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
  
  def __repr__(self):
    return f'{self.title} - {self.status}'