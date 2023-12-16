from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

url = "https://www.timeanddate.com/weather/"
res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'aboutus.html')
def second_home(request):
    return render(request, 'app.html')
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()

        return redirect('register')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('second')
        else:
            return render(request, 'login.html')


    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return render(request, 'index.html')
def weather_app(request,soup=soup):

    title = soup.find('span', class_='my-city__city')
    weather = soup.find('span', class_='my-city__temp')
    wind = soup.find('span', class_='my-city__wtdesc')
    date = soup.find('span', class_='my-city__digitalClock')
    return render(request, 'weather.html', {'city':title.text, 'weather':weather.text,'wind':wind.text,'date':date.text })

def todo_app(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list" : item_list,
        'title': "TODO_LIST",

    }
    return render(request, 'todo.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')






