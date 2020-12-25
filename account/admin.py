from django.contrib import admin

from .models import Task, Subtask


class SubtaskInline(admin.TabularInline):
    model = Subtask
    fk_name = 'task'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'worker',
                    'created', 'redline', 'deadline')
    list_filter = ('status', 'worker', 'deadline', 'redline')
    search_fields = ('name', 'redline', 'deadline', 'worker')
    ordering = ('created',)
    inlines = [SubtaskInline]
