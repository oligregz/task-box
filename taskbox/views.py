from django.shortcuts import render
from .models import Board, Task
from .serializer import BoardSerializer, TaskSerializer
from rest_framework import viewsets

# as views servem para renderizar a requisição

class BoardViewSet(viewsets.ModelViewSet):
  queryset =  Board.objects.all()
  serializer_class = BoardSerializer


class TaskViewSet(viewsets.ModelViewSet):
  queryset =  Task.objects.all()
  serializer_class = TaskSerializer
