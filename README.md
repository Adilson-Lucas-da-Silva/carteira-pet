# 🐾 Projeto Carteira Pet

Sistema web desenvolvido com **Django** para gerenciamento de pets, tutores, veterinários e vacinas.

---

## 📌 Descrição

O projeto tem como objetivo controlar informações relacionadas a:

- Tutores
- Pets
- Espécies
- Veterinários
- Vacinas

Os dados são armazenados em banco **MySQL**, com estrutura previamente definida via script SQL.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Django 6.0.3
- MySQL
- Gunicorn

---

## 📁 Estrutura do Projeto

```
Projeto1/
│
├── meuapp/              # Aplicação principal
├── meuprojeto/          # Configurações do Django
├── manage.py
├── requirements.txt
├── esquema_SQL.sql      # Script do banco de dados
└── db.sqlite3 (não utilizado)
```

---

## ⚙️ Configuração do Ambiente

### 1. Clone o projeto

```
git clone <url-do-repositorio>
cd Projeto1
```

---

### 2. Crie e ative o ambiente virtual

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Instale as dependências

```
pip install -r requirements.txt
```

---

## 🗄️ Configuração do Banco de Dados

### 1. Crie o banco no MySQL

Execute o script:

```
Esquema_SQL_Carteira_PET.sql
```

Isso irá criar o banco:

```
carteira_pet
```

---

### 2. Configure o acesso no arquivo `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carteira_pet',
        'USER': 'root',
        'PASSWORD': 'SUA_SENHA_AQUI',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🔐 Configuração da SECRET_KEY

O projeto utiliza variável de ambiente.

### Execute no Prompt de Comando (CMD) do Windows:

```
setx SECRET_KEY "sua-chave-secreta"
```

Depois:
- Feche o VSCode ou a IDE que você está usando
- Abra novamente

---

## ▶️ Execução do Projeto

Execute:

```
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 👤 Acesso ao Admin

Crie um superusuário:

```
python manage.py createsuperuser
```

Acesse:

```
http://127.0.0.1:8000/admin/
```

---

## 📊 Modelagem do Banco

O sistema possui as seguintes entidades principais:

- Usuario
- Tutor
- Pet
- Especie
- Veterinario
- Vacina

### Relacionamentos importantes:

- Tutor → Usuario
- Pet → Tutor e Especie
- Vacina → Pet e Veterinario
- Pet ↔ Veterinario (N:N)

---

## ⚠️ Observações Importantes

- As tabelas são gerenciadas externamente (MySQL)
- Os models utilizam:

```
managed = False
```

👉 Portanto:
- Não execute `makemigrations`
- Não execute `migrate` para criar tabelas

---

## 👥 Trabalho em Equipe

- Cada integrante deve configurar:
  - Sua própria senha do MySQL
  - Sua própria SECRET_KEY

- Não versionar:
  - `.venv`
  - dados sensíveis

---

## 📦 Dependências

Arquivo `requirements.txt`:

```
asgiref==3.11.1
Django==6.0.3
gunicorn==25.2.0
mysqlclient==2.2.8
packaging==26.0
PyMySQL==1.1.2
sqlparse==0.5.5
tzdata==2025.3
```

---

## 🚀 Status do Projeto

✔ Funcional  
✔ Integrado com MySQL  
✔ Pronto para uso acadêmico  

---

## 📌 Autor / Equipe

Projeto desenvolvido em grupo para fins acadêmicos.
