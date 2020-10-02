from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def root(request):
    return redirect('/blogs')
def index(request):
    return HttpResponse("Placeholder to later display all the list of blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/blogs')

def show(request, num):
    print(num)
    return HttpResponse("Placeholder to edit blog " + num + ".")

def edit(request, num):
    print(num)
    return HttpResponse("Placeholder to edit blog " + num + ".")

def destroy(request, num):
    print(num)
    return redirect('/blogs')