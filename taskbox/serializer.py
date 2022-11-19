from .models import Board, Task
from rest_framework import serializers

# serializer serve para transformar o objeto pythonico retornado da requisição na API
# e transforma em json

class BoardSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model: Board
    fields: '__all__'
    
class TaskSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model: Task
    fields: '__all__'