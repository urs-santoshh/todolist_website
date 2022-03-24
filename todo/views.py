from django.shortcuts import render
from todo.models import Task

# Create your views here.
def index(request):
    context = {"success":False}
    if request.method == "POST":
        title = request.POST["title"]
        detail = request.POST["detail"]
        ins = Task(taskTitle=title, taskDetail=detail)
        ins.save()
        context["success"] = True
    return render(request,'home.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    toDoos = {'tasks':allTasks}
    return render(request,'tasks.html',toDoos)
