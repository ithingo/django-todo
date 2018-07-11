from django.views import View
from django.http import HttpResponse
from django.template import loader

from .models import TodoItem


class TemplateView(View):
    @staticmethod
    def add_task(request):
        print(request.POST)
        if request.method == 'POST':
            if "task_add" in request.POST:
                input_text = request.POST['input_text'] + "1"

                new_task_item = TodoItem(input_text=input_text)
                new_task_item.save()

        task_list = TodoItem.objects.all()
        template = loader.get_template('polls/index.html')
        context = {
            'task_list': task_list,
        }

        return HttpResponse(template.render(context, request))

