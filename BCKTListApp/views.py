from django.shortcuts import render
from .models import Todo

def index(request):

    # Get todo list from DB, assign to context
    bckt_list = Todo.objects.order_by("id")
    context = {"bckt_list" : bckt_list}
    # Return
    return render(request, "index.html", context)
