from django.shortcuts import render, redirect
from main.models import TODO

# Create your views here.
def home(request):
    todos = TODO.objects.all()
    if request.user.is_authenticated:
        return render(request, 'main/home.html', {'todos':todos})
    else: 
        return redirect('signin')
    

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def add(request):
    if request.method == 'GET':
        return render(request, 'main/add-todo.html')
    else:
        description = request.POST['description']
        title = request.POST['title']



        TODO.objects.create(title=title, content=description, is_completed=False, user_id=1)

        return redirect('home')
    

def delete (request, id):
    todo = TODO.objects.get(id=id)
    todo.delete()

    return redirect('home')

def edit(request, id):
    todo = TODO.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'main/edit-todo.html', {'todo':todo})
    else: 
        description = request.POST['description']
        new_title = request.POST['title']

        todo = TODO.objects.get(id=id)
        todo.title = new_title
        todo.content = description

        todo.save()

        return redirect ('home')
    

def complete(request, id):
    todo = TODO.objects.get(id=id)
    if todo.is_completed:
        todo.is_completed = False
    else:
        todo.is_completed = True
    todo.save()

    return redirect('home')

