from django.db import models
from django.conf import settings

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=500)
    todo_bool = models.BooleanField(default="True")

    def __str__(self):
        return self.task

