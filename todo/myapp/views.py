from django.shortcuts import render
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")
    return render(request, 'base.html', {
        'todo_items': todo_items
    })

def add_to_do(request):
    current_date  = timezone.now()
    content = request.POST.get('content')
    models.Todo.objects.create(added_date=current_date, text=content)
    
    return HttpResponseRedirect('/')

def delete(request, todo_id):
    delete_item = models.Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect("/")
