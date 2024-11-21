from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages 
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    return render(request,'home.html')

def logoutview(request):
    logout(request)
    return redirect('login')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if both fields are provided
        if not username or not password:
            messages.error(request, 'Both fields are required.')
            return redirect('login')

        # Check if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')

        # Log in the user if authentication is successful
        login(request, user)
        return redirect('index')
    
    # If it's a GET request, render the login page
    return render(request, 'login.html')




def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.info(request,'User already exists')
            return redirect('register')
        
        user = User(
           
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect('login')    
    return render(request,'register.html')



@login_required
def index_page(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            new_todo = todo(user = request.user,todo_name = task)
            new_todo.save()
        return redirect('index')

    todos = todo.objects.filter(user = request.user)
    username = request.user.username if request.user.is_authenticated else None
    context = {
        'username' : username,
        'todos' : todos
    }
    return render(request, 'index.html',context)


@login_required
def delete_task(request,name):
    todo_item = todo.objects.get(user = request.user, todo_name = name)
    todo_item.delete()
    return redirect('index')



@login_required
def update_task(request,name):
    todo_item = todo.objects.get(user = request.user, todo_name = name)
    todo_item.status = True
    todo_item.save()
    return redirect('index')