from rest_framework import serializers


from polls import models


class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'input_text',
            'checked',
            'created_at',
            'updated_at',
        )
        model = models.TodoItem
