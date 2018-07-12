import json


from django.views.generic import View, ListView
from django.http import HttpResponse, JsonResponse
from django.template import loader


from .models import TodoItem
from .forms import NewItemForm


class MyBaseTemplateView(View):
    template_name = loader.get_template('polls/index.html')

    form_class = NewItemForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'form': form,
            'task_list': task_list,
        }

        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        print(request)

        input_text = request.POST.get('input_text', None)

        print(input_text)

        if form.is_valid():
            new_task_item = TodoItem(input_text=input_text)
            new_task_item.save()

        # task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'form': form,
            # 'task_list': task_list,
        }

        # return HttpResponse(template.render(context, request))
        return HttpResponse(template.render(context))
