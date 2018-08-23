from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


def index(request):

    # Get todo from DB, make form, assign to context
    bckt_list = Todo.objects.order_by("id")
    form = TodoForm()
    context = {"bckt_list" : bckt_list, "form": form}
    # Return
    return render(request, "index.html", context)


@require_POST
def addTodo(request):

    # Get form from request
    form = TodoForm(request.POST)
    # If form is valid, add to DB
    if form.is_valid():
        new_item = Todo(text=request.POST["text"])
        new_item.save()
    # Return: redirect to index
    return redirect("index")


def completeTodo(request, todoID):

    todo = Todo.objects.get(pk=todoID)
    todo.complete = True
    todo.save()
    return redirect("index")


def deleteCompletedTodo(request):

    # Search for and delete objects that have been completed
    Todo.objects.filter(complete__exact=True).delete()
    return redirect("index")


def deleteAll(request):

    Todo.objects.all().delete()
    return redirect("index")