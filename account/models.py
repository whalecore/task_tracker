from django.db import models
from django.conf import settings


class Task(models.Model):
    TD = 'To Do'
    INP = 'In Progress'
    TEST = 'Testing'
    DN = 'Done'
    STATUSES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Testing', 'Testing'),
        ('Done', 'Done'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUSES, default=TD)
    created = models.DateTimeField(auto_now_add=True)
    redline = models.DateTimeField()
    deadline = models.DateTimeField()
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Subtask(Task, models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.PROTECT, related_name='main_task')
