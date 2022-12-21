from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#This is to get a predefined 'User'
from django.contrib.auth.models import User
#If we want to reply with basic HTML only
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
#We want to use a Form that we created
from .forms import TodoForm
#We want to query this table
from .models import Todo
# Create your views here.
def signupuser(request):
    #Check the object coming it see what it is
    if request.method == 'GET':
        #we know they are just coming to the page
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm})
    else:
        #This is the target of a Form.  We need to do the work.
        if request.POST['password1']  == request.POST['password2']:
            try:
            #The passwords match, then we create a user
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            #This will save it into the db.  If that fails the except returns an error to the User
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm, 'error':'Username already in use'})
        else:
            print('Error creating User')
            #send them back to the signup page, but with the error
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm, 'error':'Passwords do not match'})

def currenttodos(request):
    #Create a query to get Todos that are related to this User
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/currenttodos.html',{'todos':todos})

#This view takes an arg for the primary key of the Todo object we want
def viewtodos(request, todo_pk):
    #Use the Primary Key and just get that record
    todo = get_object_or_404.(Todo, todo.pk)
    return render(request, 'todo/viewtodos.html',{'todo':todo})

def createtodos(request):
    if request.method == 'GET':
        #we know they are just coming to the page
        return render(request, 'todo/createtodos.html', {'form':TodoForm})
    else:
        #Extra security to prevent bad data
        try:
            #We are using the custom form, which is being supplied by the POST
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            #Lets add the User which actually is adding it [this comes from the request object]
            newtodo.user = request.user
            newtodo.save()
            #Send us to some new location, say the current list
            return redirect('currenttodos')
        except ValueError:
            #Send them back to the create page with the erro dictionary
            return render(request, 'todo/createtodos.html',{'form':TodoForm(),'error':"Bad data passed in"})

def home(request):
    return render(request, 'todo/home.html')

def logoutuser(request):
    #Only do this if it is a POST, not a GET to prevent accidental logging out
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
        #Check the object coming it see what it is
    if request.method == 'GET':
        #we know they are just coming to the page
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm})
    else:
        #Create a User, if they are successful
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            #It has FAILED, therefore send us back to the Login page with an Error to display
            return render(request, 'todo/loginuser.html',{'form':AuthenticationForm(), 'error':'The Username and Password were not found'})
        else:
            #We have succeeded, now simply send on their way
            login(request, user)
            return redirect('currenttodos')

