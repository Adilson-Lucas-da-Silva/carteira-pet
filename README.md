# 🐾 Carteira PET

Sistema web desenvolvido com Django para gerenciamento de pets, tutores,
veterinários e controle de vacinas.

------------------------------------------------------------------------

## 📌 Tecnologias utilizadas

-   Python 3.x
-   Django 6.0.3
-   MySQL
-   HTML (templates Django)

------------------------------------------------------------------------

## ⚠️ Importante

Este projeto **NÃO utiliza migrations do Django**.

O banco de dados deve ser criado manualmente a partir do script SQL:

    Esquema_SQL_Carteira_PET.sql

------------------------------------------------------------------------

## 🚀 Como rodar o projeto

### 1. Clone o repositório

``` bash
git clone https://github.com/Adilson-Lucas-da-Silva/carteira-pet.git
cd carteira-pet
```

------------------------------------------------------------------------

### 2. Crie e ative o ambiente virtual

``` bash
python -m venv .venv
```

#### Windows:

``` bash
.venv\Scripts\activate
```

#### Linux/Mac:

``` bash
source .venv/bin/activate
```

------------------------------------------------------------------------

### 3. Instale as dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4. Configure o banco de dados (MySQL)

Crie o banco:

``` sql
CREATE DATABASE carteira_pet;
```

Execute o script SQL:

    Esquema_SQL_Carteira_PET.sql

------------------------------------------------------------------------

### 5. Configure o arquivo settings.py

Edite o trecho:

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carteira_pet',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

------------------------------------------------------------------------

### 6. Rodar o projeto

``` bash
python manage.py runserver
```

Acesse:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🧠 Estrutura do projeto

    Projeto1/
    ├── meuapp/
    ├── meuprojeto/
    ├── Esquema_SQL_Carteira_PET.sql
    ├── manage.py
    ├── requirements.txt

------------------------------------------------------------------------

## 📊 Banco de dados

-   Usuário
-   Tutor
-   Pet
-   Espécie
-   Veterinário
-   Vacina

------------------------------------------------------------------------

## ⚠️ Observações

-   Models via inspectdb
-   managed = False
-   Alterações no banco via MySQL

------------------------------------------------------------------------

## 👨‍💻 Autor

Adilson Lucas da Silva
