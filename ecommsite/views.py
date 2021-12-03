from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
# Create your views here.

'''
def index(response, name):
    ls=ToDoList.objects.get(name=name)
    #item = ls.item_set.get(id=1)
    #return HttpResponse("<h1> %s </h1><br><p>%s</p>" %(ls.name, item.text))
    return HttpResponse("<h1> %s </h1><br><p></p>" %(ls.name))
'''
def index(response, id):
    #ls=ToDoList.objects.get(name=name)
    ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h1> %s </h1><br><p>%s</p>" %(ls.name, item.text))
    return render(response, "ecommsite/list.html", {"ls":ls})

def home(response):
    return render(response, "ecommsite/home.html", {})
