from django.contrib import admin

from .models import Project, Subtask, Task


class SubtaskInline(admin.StackedInline):
    model = Subtask
    fk_name = 'task'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task', 'status', 'worker',
                    'created', 'redline', 'deadline')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'worker', 'deadline', 'redline')
    search_fields = ('name', 'redline', 'deadline', 'worker')
    ordering = ('-created',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'worker',
                    'created', 'redline', 'deadline')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'worker', 'deadline', 'redline')
    search_fields = ('name', 'redline', 'deadline', 'worker')
    ordering = ('-created',)
    inlines = [SubtaskInline]


class TaskInline(admin.StackedInline):
    model = Task
    fk_name = 'project'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker', 'redline', 'deadline')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'redline', 'deadline')
    search_fields = ('name',)
    ordering = ('-created',)
    inlines = [TaskInline]
