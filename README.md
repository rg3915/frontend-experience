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

Estou usando CDN :)

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
```

## Roadmap

Nessa Single Page Application feita somente com Django e jQuery o usuário pode:

* Cadastrar um Contato
* Editar um Contato
* Deletar um Contato

### Detalhes de implementação

#### Cadastrar um Contato

Ao clicar no botão `+ Contato` abre-se um Modal (com valores pré-definidos, pra agilizar no efeito de demonstração) e depois tem um botão pra salvar o contato.

Tecnicamente é acionada uma função (`add_contact_post()`) escrita em jQuery e Ajax que aciona a url `"{% url 'core:contact_add' %}"` para persistir os dados em banco.

**Problema:** já temos tags do Django no meio do JS :(


#### Editar um Contato

Ao clicar no ícone `editar` abre-se um Modal com os valores já salvos no banco para que o usuário possa alterar os valores e salvar novamente.

A função (`edit_contact_post()`) é acionada para, a partir da url `"{% url 'core:contact_edit' pk=contact.pk %}"` salvar os novos dados no banco.

**Problema:** Só veja o [link](https://github.com/rg3915/frontend-experience/blob/master/myproject/core/templates/index.html#L179-L180) pra ranger os dentes :(

#### Deletar um Contato

Mesma situação *editar*: comandos do Django no meio do JS.


## Endpoints da api

...