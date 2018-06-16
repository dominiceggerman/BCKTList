from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def index(request):

    # Get todo from DB, make form, assign to context
    bckt_list = Todo.objects.order_by("id")
    form = TodoForm()
    context = {"bckt_list" : bckt_list, "form": form}
    # Return
    return render(request, "index.html", context)
