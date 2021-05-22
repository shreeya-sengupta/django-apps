from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


# Create your views here.
def todoView(request):
	all_tasks = TodoItem.objects.all()
	response_content = {'all_tasks': all_tasks}
	return render(request, 'todo.html', response_content)

def addTodo(request):
	content_title = request.POST['content_title']
	content = request.POST['content']
	new_task = TodoItem(content_title=content_title, content=content)
	new_task.save()
	return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/todo/')

def editTodo(request, todo_id):
	task_to_edit1 = TodoItem.objects.get(id=todo_id)
	return render(request, 'update.html', context={'task_to_edit1': task_to_edit1})
	

def updateTodo(request, task_id):
	edited_content_title = request.POST['edited_content_title']
	edited_content = request.POST['edited_content']
	task_to_edit = TodoItem.objects.get(id=task_id)
	task_to_edit.content_title = edited_content_title
	task_to_edit.content = edited_content
	task_to_edit.save()
	return HttpResponseRedirect('/todo/')

