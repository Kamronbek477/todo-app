from django.urls import path
from .views import TaskListView,TaskIdView,TaskDoneView,TaskUndoneView, UserListView

urlpatterns = [
    path("tasks/", TaskListView.as_view()),
    path('tasks/<int:id>',TaskIdView.as_view()),
    path('tasks/<int:id>/done',TaskDoneView.as_view()),
    path('tasks/<int:id>/undone',TaskUndoneView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:id>', UserListView.as_view()),
]
