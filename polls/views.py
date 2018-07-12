import json

from django.shortcuts import render
from django.views.generic import View, ListView

from rest_framework import generics
from django.http import JsonResponse


from .forms import NewItemForm
from .models import TodoItem
from .serializers import TodoItemSerializer


class MyBaseTemplateView(View):
    template_name = 'polls/index.html'
    form_class = NewItemForm

    def get(self, request):
        form = self.form_class()

        task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'form': form,
            'task_list': task_list,
        }
        return render(request, template, context)

    def post(self, request):
        form = self.form_class(request.POST)
        input_text = request.POST.get('input_text', None)

        if form.is_valid():
            new_task_item = TodoItem(input_text=input_text)
            new_task_item.save()
            form = self.form_class()

        task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'form': form,
            'task_list': task_list,
        }
        return render(request, template, context);


class TaskList(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
