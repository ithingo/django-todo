from django.shortcuts import render
from django.views.generic import View

from .models import TodoItem
from . import forms


class MyBaseTemplateView(View):
    template_name = 'polls/index.html'
    new_item_form_class = forms.NewItemForm
    tab_switch_form = forms.TabSwitchForm

    def __get_all_objects(self):
        """Gets all task items"""
        return TodoItem.objects.all()

    def __get_checked_objects(self):
        """Gets all task items"""
        return TodoItem.objects.filter(checked=True)

    def __get_object(self, pk):
        """Gets single task by primary key (id)"""
        return TodoItem.objects.get(pk=pk)

    def __save_task(self, input_text):
        """Creates new task item from input text"""
        new_task_item = TodoItem(input_text=input_text)
        new_task_item.save()

    def __delete_task(self, pk):
        """Deletes task from db by primary key (id)"""
        task = self.__get_object(pk)
        task.delete()

    def __change_task_status(self, pk, checked):
        """Changes task status - checked or unchecked"""
        task = self.__get_object(pk)
        task.checked = checked
        task.save()

    def __change_all_status(self, checked):
        tasks = self.__get_all_objects()
        for task in tasks:
            task.checked = checked
            task.save()

    def __delete_all(self):
        tasks = self.__get_checked_objects()
        tasks.delete()

    # HTML forms support only GET and POST methods

    def get(self, request):
        """For method GET"""
        tab_switch_form = forms.TabSwitchForm()
        new_item_form = forms.NewItemForm()

        task_list = self.__get_all_objects()

        if 'tabs' in request.GET:
            selection = request.GET.get('tabs')
            if selection == 'all':
                task_list = self.__get_all_objects()
            if selection == 'checked':
                task_list = task_list.filter(checked=True)
            if selection == 'unchecked':
                task_list = task_list.filter(checked=False)

        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)

    def post(self, request):
        """For method POST"""
        tab_switch_form = forms.TabSwitchForm(request.POST)
        new_item_form = forms.NewItemForm(request.POST)

        if 'add_item' in request.POST:
            if new_item_form.is_valid():
                input_text = new_item_form.cleaned_data['input_text']
                self.__save_task(input_text)
                new_item_form = forms.NewItemForm()

        if 'delete_item' in request.POST:
            pk = request.POST.get('task_id')
            self.__delete_task(pk)

        if 'make_item_done' in request.POST:
            pk = request.POST.get('task_id')
            checked = True
            self.__change_task_status(pk, checked)

        if 'make_item_undone' in request.POST:
            pk = request.POST.get('task_id')
            checked = False
            self.__change_task_status(pk, checked)

        if 'select_all' in request.POST:
            checked = True
            self.__change_all_status(checked)

        if 'deselect_all' in request.POST:
            checked = False
            self.__change_all_status(checked)

        if 'delete_all' in request.POST:
            self.__delete_all()

        task_list = self.__get_all_objects()
        template = self.template_name
        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list,
        }
        return render(request, template, context)




