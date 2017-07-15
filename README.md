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

## Endpoints da api

