"# feladatkezelés kész, fiók kezelés nincs" 
Ha kiprobálnád:
-kell egy virtuális fejlesztő környezet
    mkdir django_env; cd django_env
    pythom -m venv . 
-telepíteni kell a django-t
    pip install django
-létre kell hozni a project mappáját
    mkdir project; cd project
-el kell készíteni a django "magját"
    django-admin startproject _core .
-a _core azért kell mert így több alkalmazást is tudunk tlepíteni a projectb(blog, webshop)
-clónozd egy mappába a mainsite-ot a _core-ral egy mappába
    
  
