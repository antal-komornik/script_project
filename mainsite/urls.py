from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos, name="tds"),
    path("<int:pk>/", views.todo, name="td"),
]
