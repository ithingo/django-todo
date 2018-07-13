from rest_framework import serializers


from polls import models


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'input_text',
            'checked',
            'created_at',
            'updated_at',
        )
        model = models.Task
