# 🐾 Projeto Carteira Pet

Sistema web desenvolvido com **Django** para gerenciamento de pets, tutores, veterinários e vacinas.

---

## 📌 Descrição

O **Carteira Pet** é um sistema web acadêmico desenvolvido para auxiliar no gerenciamento de informações relacionadas a pets e seus responsáveis, permitindo o cadastro e acompanhamento de:

- Tutores
- Pets
- Espécies
- Veterinários
- Vacinas

O sistema utiliza **Python com Django** integrado ao **MySQL**, adotando um modelo híbrido de banco de dados:

- As tabelas do domínio do sistema são criadas por **script SQL gerado a partir do MER (Modelo Entidade-Relacionamento)**.
- O Django é utilizado apenas para gerenciamento da aplicação e de suas tabelas internas de autenticação e sessão.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Django 6.0.3
- MySQL
- Gunicorn
- HTML5
- CSS3
- Bootstrap

---

## ✅ Pré-requisitos

Antes de iniciar, tenha instalado:

- Python 3.x
- MySQL Server
- MySQL Workbench (opcional)
- Git

---

## 📁 Estrutura do Projeto

```text
Carteira_Pet/
│
├── meuapp/                            # Aplicação principal
├── meuprojeto/                       # Configurações do Django
├── static/                           # Arquivos estáticos
├── manage.py
├── requirements.txt
├── Esquema_SQL_Carteira_PET.sql      # Script de criação do banco
├── Dados_Carteira_Pet_Sem_Django.sql # Script de carga de dados
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1. Clone o projeto

```bash
git clone <url-do-repositorio>
cd Carteira_Pet
```

---

### 2. Crie e ative o ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do Banco de Dados

### 1. Crie o banco de dados no MySQL

Execute o script:

```text
Esquema_SQL_Carteira_PET.sql
```

Este script foi gerado a partir do **MER (Modelo Entidade-Relacionamento)** criado no **MySQL Workbench** e é responsável pela criação das tabelas do domínio da aplicação, tais como:

- tutor
- pet
- especie
- veterinario
- vacina
- usuario

Após a execução do script, será criado o schema:

```sql
carteira_pet
```

---

### 2. Configure o acesso ao banco no arquivo `settings.py`

Edite o arquivo:

```text
meuprojeto/settings.py
```

Ajuste as credenciais do banco de dados conforme o seu ambiente:

```python
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

### 3. Execute as migrações do Django

Após criar o banco do sistema via SQL, execute:

```bash
python manage.py migrate
```

### Importante

Este comando **não recria as tabelas do sistema Carteira Pet**.

Ele é utilizado **somente para criação das tabelas internas do Django**, necessárias para:

- autenticação de usuários (`auth_*`)
- permissões
- sessões (`django_session`)
- logs administrativos
- gerenciamento interno do framework

Exemplos de tabelas criadas pelo Django:

```text
auth_user
auth_group
django_session
django_admin_log
django_content_type
django_migrations
```

As tabelas do sistema **não são gerenciadas pelo ORM do Django**, pois os models utilizam:

```python
managed = False
```

Por este motivo:

✅ Execute `migrate` para as tabelas do Django.
❌ Não utilize `makemigrations` para recriar as tabelas do sistema.

---

### 4. Execute a carga de dados do projeto

Somente **após executar o comando `migrate`**, rode o script:

```text
Dados_Carteira_Pet_Sem_Django.sql
```

Este script insere dados iniciais no banco para testes e utilização do sistema.

**Atenção:** conforme o próprio nome indica (**Sem_Django**), ele não cria estruturas do Django e pressupõe que as tabelas internas do framework já tenham sido criadas anteriormente.

---

## 🔐 Configuração da SECRET_KEY

O projeto utiliza variável de ambiente para segurança.

### Execute no Prompt de Comando (CMD) do Windows:

```bash
setx SECRET_KEY "sua-chave-secreta"
```

Depois:

- Feche o VSCode (ou IDE utilizada)
- Abra novamente

---

## ▶️ Execução do Projeto

Execute:

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

---

## 👤 Administração do Django

Crie o Superusuário de Administração do Django através do comando abaixo. Durante a execução, serão solicitados:

- Usuário
- Senha
- E-mail (opcional)

```bash
python manage.py createsuperuser
```

Acesse:

```text
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

### Relacionamentos importantes

- Tutor → Usuario
- Pet → Tutor e Especie
- Vacina → Pet e Veterinario
- Pet ↔ Veterinario (N:N)

---

## ⚠️ Observações Importantes

- O banco de dados principal é gerenciado via **MySQL e SQL manual**.
- O Django é utilizado apenas como framework da aplicação e para suas tabelas internas.
- Os models utilizam:

```python
managed = False
```

- O script `Esquema_SQL_Carteira_PET.sql` deve ser executado antes do `migrate`.
- O script `Dados_Carteira_Pet_Sem_Django.sql` deve ser executado somente após o `migrate`.

---

## 👥 Trabalho em Equipe

Cada integrante do grupo deve configurar:

- Sua própria senha do MySQL
- Sua própria `SECRET_KEY`

Não versionar:

- `.venv`
- credenciais
- arquivos sensíveis

---

## 📦 Dependências

As dependências do projeto encontram-se no arquivo:

```text
requirements.txt
```

---

## 🚀 Status do Projeto

✔ Funcional
✔ Integrado com MySQL
✔ Pronto para uso acadêmico

---

## 📌 Contextualização Acadêmica

Projeto acadêmico desenvolvido no contexto da disciplina de **Projeto Integrador I**, do curso do **Eixo de Computação da Universidade Virtual do Estado de São Paulo (UNIVESP)**.

Este repositório acompanha o desenvolvimento técnico do sistema e complementa o **Relatório Técnico-Científico apresentado na disciplina de Projeto Integrador I**.
