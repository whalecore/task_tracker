from django.conf import settings
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField('project name', max_length=200)
    slug = models.SlugField(max_length=200)
    redline = models.DateTimeField()
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("project", kwargs={"project_slug": self.slug})
    


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
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUSES, default=TD)
    created = models.DateTimeField(auto_now_add=True)
    redline = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("task", kwargs={"task_slug": self.slug})
    


class Subtask(models.Model):
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
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUSES, default=TD)
    created = models.DateTimeField(auto_now_add=True)
    redline = models.DateTimeField()
    deadline = models.DateTimeField()
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    task = models.ForeignKey(
        Task, on_delete=models.PROTECT, related_name='subtasks')

    def __str__(self) -> str:
        return self.name
