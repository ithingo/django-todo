from django.shortcuts import render
from django.views.generic import View


from .forms import NewItemForm
from .models import TodoItem


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

