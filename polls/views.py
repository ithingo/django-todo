from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import TodoItem


def index(request):
    task_list = TodoItem.objects.order_by('-created_at')[:6]
    template = loader.get_template('polls/index.html')
    context = {
        'task_list': task_list,
    }
    return HttpResponse(template.render(context, request))
