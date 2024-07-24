from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('hello world!, You are at coffee with django home page')
    return render(request, 'website/index.html')  #request and path

def about(request):
    # return HttpResponse('hello world!, You are at coffee with django about page')
    return render(request, 'website/index.html')

def contact(request):
    return HttpResponse('hello world!, You are at coffee with django contact page')

# pip install uv                            --- to install uv
# uv venv                                   --- to create virtual environment
# uv pip install packagename                --- to install a package into the virtual environment(eg: Django)

# django-admin startproject projectname     --- to create project(used only once)
# cd projectname
# py manage.py runserver                    --- to run server, manage.py is the python file 

# create views file to define functions and logic
# connect views methods to urls.py

# To create templates create templates folders in root directory of working directory, it's used to 
# store html files
# Create static folder in root directory(to store css and js files)
# to use static file load it and use it then import os in settings and 
#  set the static directory

