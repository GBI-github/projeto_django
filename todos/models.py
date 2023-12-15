from django.db import models

class Todo(models.Model):
    title =  models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.TimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)

