<h1><img src = "https://imgur.com/NtK37qh.png" width="20%"/></h1>

<strong>Django</strong> é um framework para desenvolvimento rápido para web, escrito em <strong>Python</strong>, que utiliza o padrão model-template-view.

Esse framework dispõe de uma arquitetura de alto nível, o que significa que você poderá colocar os seus projetos Python na web, sem se preocupar com a infraestrutura de código necessária para isso.

Se você não conhece Python, você pode querer começar entendendo como a linguagem é. 

O <strong>Django</strong> é 100% Python, por isso, se você se sente pelo menos um pouco confortável com Python, você provavelmente irá obter muito mais do Django.

<h1>Fazendo deploy:</h1>

Se você não tem prática com o Heroku, <strong>comentar</strong> as seguintes linhas abaixo em <strong>mysite ➔ settings.py</strong> para funcionamento local.

<p><em>import django_heroku ⛔</em></p>
<p><em>django_heroku.settings(locals()) ⛔</em></p>

* python -m venv myvenv ⤵
* myvenv\Scripts\activate 
* python -m pip install Django
* python manage.py migrate
* python manage.py makemigrations polls
* python manage.py sqlmigrate polls 0001
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver ✔

<h1>Fazendo deploy com Heroku:</h1>

Caso tenha prática com o Heroku ou queira aprender, <strong>descomentar</strong> as seguintes linhas abaixo em <strong>mysite ➔ settings.py</strong> para funcionamento da aplicação via web.

<p><em>import django_heroku ✅</em></p>
<p><em>django_heroku.settings(locals()) ✅</em></p>

* python -m venv myvenv ⤵
* myvenv\Scripts\activate
* pip install Django, gunicorn, django-heroku
* heroku login
* heroku apps:create 'nome do aplicativo'
* git init
* heroku git:remote 'nome do aplicativo'
* git status
* git add .
* git commit -m 'nome do comentário'
* git push -u heroku master
* heroku run python manage.py migrate
* heroku run python manage.py makemigrations polls
* heroku run python manage.py sqlmigrate polls 0001
* heroku run python manage.py migrate
* heroku run python manage.py createsuperuser ✔

<h1>Teste:</h1>

* https://devops-django.herokuapp.com/ 💻
* Usuário: admin
* Senha: admin
