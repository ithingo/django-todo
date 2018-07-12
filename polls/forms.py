from django import forms


from .models import TodoItem


class NewItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('input_text',)
