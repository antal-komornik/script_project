"# feladatkezelés kész, fiók kezelés nincs" 
Ha kiprobálnád:
-kell egy virtuális fejlesztő környezet:
    mkdir django_env; cd django_env
    pythom -m venv . 
-telepíteni kell a django-t:
    pip install django
-létre kell hozni a project mappáját:
    mkdir project; cd project
-el kell készíteni a django "magját":
    django-admin startproject _core .
-a _core azért kell mert így több alkalmazást is tudunk tlepíteni a projectb(blog, webshop):
-clónozd egy mappába a mainsite-ot a _core-ral egy mappába:
    git clone git@github.com:antal-komornik/script_project.git 
-aktiválni kell a vurtuáélis környezetet:
    env\Scripts\activate
-a _core/settings.py -ba az "installed Apps"- hez írd be "mainsite",
-a _core/urls.py-ba írd be a "path" mellé, hogy ", include",
-importáld a _core-ba a mainsite/urls.py-t:
    path("todos/", include(mainsite.urls))
-az adatbázis léterehozásához:
    python manage.py makemigrations
    pathon manage.py migrate
-az oldal elindításához:
    python manage.py runserver
-az oldal elérhető:
    http://127.0.0.1:8000/todos/
