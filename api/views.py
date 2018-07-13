from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from polls.models import Task
from api.serializers import TaskSerializer


class TaskList(APIView):
    """
        List all tasks (or creates it)
    """
    def get_all_objects(self):
        try:
            return Task.objects.all()
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)

    def post(self, request, format=None):
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        tasks = self.get_all_objects()
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetails(APIView):
    """
        Retrieve, update or delete tasks
    """
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data)

    def post(self, request, pk, format=None):
        task = self.get_object(pk)
        task_serializer = TaskSerializer(task, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)