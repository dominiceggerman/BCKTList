from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addTodo, name="add"),
    path("complete/<todoID>", views.completeTodo, name="complete"),
    path("deletecompletedtodo", views.deleteCompletedTodo, name="deletecompletedtodo"),
    path("deleteall", views.deleteAll, name='deleteall')
]