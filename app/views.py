from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test
from .models import Task,Stage,Project
from .forms import TaskForm


def is_in_group(user):
    return user.groups.filter(name__in=['Stage_Owner', 'PM']).exists()


# Create your views here.
@user_passes_test(is_in_group)
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')  
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})


def render_task_by_stage(request,stage_id):
      stage = get_object_or_404(Stage, pk=stage_id)

      tasks = Task.objects.filter(stage_id=stage_id)

      template = loader.get_template('tasks.html')
      context = {
      'stage':stage,
      'tasks': tasks,
    
  }
      return HttpResponse(template.render(context, request))

def render_all_task(request):
      tasks = Task.objects.all()
      template = loader.get_template('tasks.html')
      context = {
            'tasks':tasks,
      }
      return HttpResponse(template.render(context, request))
