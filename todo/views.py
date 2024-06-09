from django.shortcuts import render, redirect
from todo.froms import TodoForm, TodoRemove
from todo.models import Task
from django.contrib import messages

# Create your views here.

def dashboard(request):
    users = Task.objects.all().order_by('-date')
    return render(request,'index.html',{'users': users})

def add_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request,'add_task.html',{'form':form})

def delete_task(request):
    if request.method == 'POST':
        form = TodoRemove(request.POST)
        if form.is_valid():
            user = form.cleaned_data['name']
            data = Task.objects.filter(name__icontains = user)
            if not data:
                messages.info(request,'Task Is Not Avaliable.')
            return render(request,'delete_task.html',{"data":data})
    form = TodoRemove()
    return render(request,'delete_task.html')

def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('remove')  

def search(request):
    if request.method == 'POST':
        form = TodoRemove(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            user = Task.objects.filter(name__icontains = data)
            return render(request,'index.html',{'users':user})
    form = TodoRemove()
    return  render(request,'index.html',{"users":form})