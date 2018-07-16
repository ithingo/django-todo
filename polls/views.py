from django.shortcuts import render
from django.views.generic import View

from .models import TodoItem
from . import forms


class MyBaseTemplateView(View):
    template_name = 'polls/index.html'
    success_url = '/'

    new_item_form_class = forms.NewItemForm
    tab_switch_form = forms.TabSwitchForm

    def get_all_objects(self):
        try:
            return TodoItem.objects.all()
        except TodoItem.DoesNotExist:
            return None                   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def get_object(selfself, pk):
        try:
            task = TodoItem.objects.get(pk=pk)
            return task
        except TodoItem.DoesNotExist:
            return None                   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def get(self, request):
        tab_switch_form = forms.TabSwitchForm()
        new_item_form = forms.NewItemForm()

        task_list = self.get_all_objects()
        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)

    def post(self, request):
        tab_switch_form = forms.TabSwitchForm(request.POST)
        new_item_form = forms.NewItemForm(request.POST)

        if 'add_item' in request.POST:
            if new_item_form.is_valid():
                input_text = new_item_form.cleaned_data['input_text']
                self.save_task(input_text)
                new_item_form = forms.NewItemForm()

        if 'delete_item' in request.POST:
            pk = request.POST.get('task_id')
            self.delete_task(pk)

        if 'make_item_done' in request.POST:
            pk = request.POST.get('task_id')
            checked = True
            self.change_task_status(pk, checked)

        if 'make_item_undone' in request.POST:
            pk = request.POST.get('task_id')
            checked = False
            self.change_task_status(pk, checked)

        task_list = self.get_all_objects()
        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)

    def save_task(self, input_text):
        new_task_item = TodoItem(input_text=input_text)
        new_task_item.save()

    def delete_task(self, pk):
        task = self.get_object(pk)
        task.delete()

    def change_task_status(self, pk, checked):
        task = self.get_object(pk)
        task.checked = checked
        task.save()



