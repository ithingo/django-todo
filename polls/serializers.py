from rest_framework import serializers


from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'input_text', 'checked', 'created_at', 'updated_at',)
        model = TodoItem
