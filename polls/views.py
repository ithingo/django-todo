from django.shortcuts import render
from django.views.generic import View

from .models import TodoItem
from . import forms


class MyBaseTemplateView(View):
    template_name = 'polls/index.html'
    success_url = '/'

    def get(self, request):
        tab_switch_form = forms.TabSwitchForm(prefix='tabs')
        new_item_form = forms.NewItemForm(prefix='newi')



        task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)

    def post(self, request):
        tab_switch_form = forms.TabSwitchForm(request.POST, prefix='tabs')
        new_item_form = forms.NewItemForm(request.POST, prefix='newi')

        input_text = request.POST.get('input_text', None)

        if new_item_form.is_valid() and tab_switch_form.is_valid():

            # print(request.POST)

            new_task_item = TodoItem(input_text=input_text)
            new_task_item.save()
            new_item_form = forms.NewItemForm()

        task_list = TodoItem.objects.all()
        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)

