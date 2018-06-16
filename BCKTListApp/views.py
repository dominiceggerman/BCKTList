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

    form = TodoForm(request.POST)
    # Return
    return redirect("index")