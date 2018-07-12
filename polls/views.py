from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import TodoItem
from .forms import NewItemForm


PAGINATION_COUNT = 5


# class MyTemplate(TemplateView):
#     def index(self, request):
#         task_list = TodoItem.objects.all()
#         template = loader.get_template('polls/index.html')
#         context = {
#             'task_list': task_list,
#         }
#
#         return HttpResponse(template.render(context, request))
#
#
# class FormInput(FormView):
#     template = loader.get_template('polls/input_form.html')
#     form = NewItemForm()
#
#     # render form with template - ??
#
#     def add_item(self, request, form=form):
#
#         if request.method == 'POST':
#
#
#             if form.is_valid():
#                 new_task_item = TodoItem(input_text=input_text)
#                 new_task_item.save()
#

class MyBaseTemplateView(TemplateView):
    base_template = loader.get_template('polls/index.html')

    form_class = NewItemForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        input_text = request.POST.get('input_text', None)

        if form.is_valid():
            new_task_item = TodoItem(input_text=input_text)
            new_task_item.save()



# class TaskListView(ListView):
#     model = TodoItem
#     paginate_by = PAGINATION_COUNT
#
#     def get_context_data(self, *, object_list=None, **kwargs):
