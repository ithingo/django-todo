from django.db import models
from django.utils import timezone as date


class TodoItem(models.Model):
    input_text = models.TextField(blank=True)
    checked = models.BooleanField(default=False)
    created_at = models.DateField(default=date.now().strftime('%Y-%m-%d'))
    updated_at = models.DateField(default=date.now().strftime('%Y-%m-%d'))

    class Meta:
        verbose_name = 'TodoItem'
        verbose_name_plural = 'TodoItems'

        # Ordering by DESC with leading "-"
        ordering = ["-created_at"]

        db_table = 'django_todo_items'

    def __str__(self):
        return "{0} ({2}) - {1}".format(self.id, self.input_text, self.checked)
