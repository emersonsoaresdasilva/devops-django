<h1><img src = "https://imgur.com/NtK37qh.png" width="20%"/></h1>

<h1>Publicando um site Django:</h1>

O <strong>Django</strong> é 100% Python, por isso, se você se sente pelo menos um pouco confortável com Python, você provavelmente irá obter muito mais do Django.

<h1>Fazendo deploy com Heroku:</h1>

* <code>python -m venv myvenv</code> ⤵
* <code>myvenv\Scripts\activate</code>
* <code>pip install Django, gunicorn, django-heroku, django-pytest</code>
* <code>heroku login</code>
* <code>heroku apps:create 'nome do aplicativo'</code>
* <code>git init</code>
* <code>heroku git:remote 'nome do aplicativo criado'</code>
* <code>git status</code>
* <code>git add .</code>
* <code>git commit -m 'comentário'</code>
* <code>heroku config:set DISABLE_COLLECTSTATIC=1</code>
* <code>git push -u heroku master</code>✔

<h1>Teste:</h1>

* https://python-pro-django.herokuapp.com/ 💻