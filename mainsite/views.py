from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todos(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tds")
    else:
        form = TodoForm()

    todos = Todo.objects.filter(allapot=False)

    return render(request, "index.html",
                  {"todos": todos,
                   "form": form, })


def todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    change_status = request.GET.get("change_status", "")

    if change_status:
        todo.allapot = True
        todo.save()
        return redirect("tds")
    return render(request, "todo.html", {"todo": todo})
