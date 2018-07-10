from django.db import models
from django.utils import timezone as date


class TodoItem(models.Model):
    text = models.TextField(blank=True)
    checked = models.BooleanField(default=False)
    created_at = models.DateField(default=date.now().strftime('%Y-%m-%d'))
    updated_at = models.DateField(default=date.now().strftime('%Y-%m-%d'))

    @property
    def text(self):
        """Returns text value had been got from input field"""
        return '%s' % self.text

    @property
    def is_checked(self):
        """Returns status of task"""
        # return '%s' % self.checked.lower()  # " 'true' instead of 'True' for JS"
        return self.checked

    @property
    def item_id(self):
        """Returns item id from table"""
        return self.id

    class Meta:
        verbose_name = 'TodoItem'
        verbose_name_plural = 'TodoItems'

        # Ordering by DESC with leading "-"
        ordering = ["-created_at"]

        db_table = 'django_todo_items'

    def __str__(self):
        return '%d -- %s' % self.id, self.text
