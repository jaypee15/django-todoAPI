from .views import ListTodo, DetailTodo

urlpatterns = [
	path("", ListTodo.as_view(), name="todo_list"),
	path("<int:pk>/", DetailTodo.as_view(), names="todo_list"),
]