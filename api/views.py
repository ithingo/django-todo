from rest_framework import generics


from polls import models as polls_models
from api.serializers import TodoItemSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = polls_models.TodoItem.objects.all()
    serializer_class = TodoItemSerializer

