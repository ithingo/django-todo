from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


from .models import TodoItem
from . import forms


import re


class MyBaseTemplateView(View):
    template_name = 'polls/index.html'
    new_item_form_class = forms.NewItemForm
    tab_switch_form = forms.TabSwitchForm

    def __get_all_objects(self):
        """Gets all task items"""
        return TodoItem.objects.all().order_by('id')

    def __get_objects_by_checked(self, checked):
        """Gets all task items"""
        return TodoItem.objects.filter(checked=checked)

    def __get_object(self, pk):
        """Gets single task by primary key (id)"""
        task = get_object_or_404(TodoItem, pk=pk)
        return task
        # return TodoItem.objects.get(pk=pk)

        # try:
        #     comment = Comment.objects.get(pk=comment_id)
        # except Comment.DoesNotExist:
        #     comment = None

    def __add_new_task(self, input_text):
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
        """Changes status - cvhecked or unchecked - for all tasks"""
        tasks = self.__get_all_objects()
        for task in tasks:
            task.checked = checked
            task.save()

    def __delete_all(self):
        """Deletes all tasks"""
        tasks = self.__get_objects_by_checked(checked=True)
        tasks.delete()

    def __get_paginated_list(self, request, task_list):
        """Returns list of elements paginated with specific page"""
        items_on_page = 5
        paginator = Paginator(task_list, items_on_page)

        try:
            page = int(request.GET.get('page', 1))
        except PageNotAnInteger:
            page = 1

        try:
            task_list_paginated = paginator.page(page)
        except(EmptyPage, InvalidPage):
            task_list_paginated = paginator.page(paginator.num_pages)

        return task_list_paginated

    def __clear_input(self, input_text):
        """Removes html tags to save only inner tag value"""
        input_text = re.sub(r'</?[a-zA-Z]*>', '', input_text)
        return input_text

    def __get_counters(self):
        """Returns dictionary with current counters for every element status type"""
        all_count = self.__get_all_objects().count()
        checked_count = self.__get_objects_by_checked(checked=True).count()
        unchecked_count = self.__get_objects_by_checked(checked=False).count()
        return {
            'all': all_count,
            'checked': checked_count,
            'unchecked': unchecked_count,
        }

    def __update_with_value(self, new_value, pk):
        task = self.__get_object(pk)
        task.input_text = new_value
        task.save()

    # HTML forms support only GET and POST methods

    def get(self, request):
        """For method GET
        renders page at first step, if tabs clicked - do tab switching
        (tab switching doesn't modify db, so it uses GET request)"""
        tab_switch_form = forms.TabSwitchForm()
        new_item_form = forms.NewItemForm()
        ghost_input_form = forms.GhostInputForm()

        task_list = self.__get_all_objects()

        if 'tabs' in request.GET:
            selection = request.GET.get('tabs')
            if selection == 'all':
                task_list = self.__get_all_objects()
            if selection == 'checked':
                task_list = task_list.filter(checked=True)
            if selection == 'unchecked':
                task_list = task_list.filter(checked=False)

        task_list_paginated = self.__get_paginated_list(request, task_list)
        template = self.template_name
        counters = self.__get_counters()

        context = {
            'tab_switch_form': tab_switch_form,
            'new_item_form': new_item_form,
            'task_list': task_list_paginated,
            'counters': counters,
            'ghost_input_form': ghost_input_form,
        }
        return render(request, template, context)

    def post(self, request):
        """For method POST
        handles POST requests from all forms on a page (all targets to the root url)
        does whatever it needs
        and re-render page"""
        new_item_form = forms.NewItemForm(request.POST)

        if 'add_item' in request.POST:
            if new_item_form.is_valid():
                input_text = new_item_form.cleaned_data['input_text']
                input_text = self.__clear_input(input_text)
                self.__add_new_task(input_text)

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

        if 'update_item' in request.POST:
            new_value = request.POST.get('input_text')
            new_value = self.__clear_input(new_value)
            pk = request.POST.get('task_id')
            self.__update_with_value(new_value, pk)

        return HttpResponseRedirect("/")