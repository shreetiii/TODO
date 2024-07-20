from django.shortcuts import render
from main.models import TODO

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

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

        print(request.POST)



        TODO.objects.create(title=title, content=description, is_completed=False, user_id=1)