from django.shortcuts import render, redirect
from main.models import TODO

# Create your views here.
def home(request):
    todos = TODO.objects.all()
    print(todos)
    return render(request, 'main/home.html', {'todos':todos})

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

        return redirect('http://127.0.0.1:8000/')