from django.urls import path
from app.views import  todo_detail_change_and_delete, TodoList #todo_list,


urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>/', todo_detail_change_and_delete),
]