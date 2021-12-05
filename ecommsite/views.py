from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import CreateNewList

def index(response, id):
    #ls=ToDoList.objects.get(name=name)
    ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h1> %s </h1><br><p>%s</p>" %(ls.name, item.text))
    return render(response, "ecommsite/list.html", {"ls":ls})

def home(response):
    return render(response, "ecommsite/home.html", {})

def create(response):
    if response.method== "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
        print(t.id)
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "ecommsite/create.html", {"form":form})

