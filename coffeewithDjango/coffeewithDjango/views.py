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
# python3 manage.py runserver                    --- to run server, manage.py is the python file 

# create views file to define functions and logic
# connect views methods to urls.py

# To create templates create templates folders in root directory of working directory, it's used to 
# store html files
# Create static folder in root directory(to store css and js files)
# to use static file load it and use it then import os in settings and 
#  set the static directory


# To create app and to run server we need manage.py file 
# To create app use < python3 manage.py startapp app_name >
# Now tell the main project that there is a new app
# create a templates folder for html files, inside it create a folder with name similar to app name,
#  we can use any name but this is industry standard, now we can create html templates
# Tell the urls.py that there is a new route through new app using the include() method by importing it
# create urls.py file and copy the urls.py code from main project and use it here to make url routes

# jinja
# To use same html layout in multiple apps(like using same nav bar, footer etc) we can use jinja templating engine
# In main project templates folder create a layout.html file, 
# then use unnamed blocks {%block name%}{%endblock%} wherever needed, 
# we can use this file in any app using extends block {%extends 'layout.html'%}
# using the name of the block we can change the content in it in the apps html pages we created

# taiwind and admin panel (refer docs)


