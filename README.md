# frontend-experience

Separando as responsabilidades do backend e do frontend numa aplicação com Django, Ajax e jQuery.

## Como rodar a aplicação

```
git clone https://github.com/rg3915/frontend-experience.git
cd frontend-experience
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin"
python manage.py runserver
```

## Bibliotecas do jQuery e Bootstrap

Eu poderia pegar as bibliotecas de uma CDN...

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
```

... mas eu baixei todos eles.

## Endpoints da api

