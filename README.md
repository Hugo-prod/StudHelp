# Stud'Help

Stud'help est un gestionnaire de cours écrit en Python3 avec le framework Django

### Installation

Cloner le dépot
```sh
$ git clone git@github.com:Hugo-prod/StudHelp.git
```

Créer un environnement virtuel
```sh
$ cd StudHelp
virtualenv .venv
```

Activer l'environnement virtuel
```sh
$ source .venv/bin/activate
```

Installer les dépendances
```sh
$ pip install -R requirements.txt
```

Initialiser la DB
```sh
$ ./manage.py makemigrations && ./manage.py migrate
```

Démarrer Stud'Help
```sh
$ ./manage.py runserver
```

### Dépendances
* [Django] - Framework Python
* [Twitter Bootstrap 4] - Framework CSS
* [Django-Bootstrap4] - Génération des formulaires en Bootstrap
* [Modular Admin] - Dashboard CSS
* [Django-Ckeditor] - Editeur de texte amélioré
* [Django-EasyPdf] - Génération d'un PDF



License
----

MIT

[Django]: <https://github.com/django/django>
[Twitter Bootstrap 4]: <http://twitter.github.com/bootstrap/>
[Django-Bootstrap4]: <https://github.com/zostera/django-bootstrap4>
[Modular admin]: <https://github.com/modularcode/modular-admin-html>
[Django-Ckeditor]: <https://github.com/dwaiter/django-ckeditor>
[Django-EasyPdf]: <https://github.com/nigma/django-easy-pdf>