from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, UserRegistrationForm, TaskForm, SubtaskForm
from .models import Project, Subtask, Task


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'account/dashboard.html', {'section': dashboard, 'projects': projects})


@login_required
def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    tasks = project.task_set.all()
    # if request.method == 'POST':
    #     form = ChangeTaskWorkerForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = ChangeTaskWorkerForm()
    return render(request, 'account/tasks.html', {'project': project, 'tasks': tasks})


@login_required
def task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    subtasks = task.subtasks.all()
    return render(request, 'account/task.html', {'task': task, 'subtasks': subtasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            cd = task_form.cleaned_data
            new_task = task_form.save(commit=False)
            new_task.save()

            return redirect(new_task.get_absolute_url())
    else:
        task_form = TaskForm()

    return render(request, 'account/create_task.html', {'task_form': task_form})