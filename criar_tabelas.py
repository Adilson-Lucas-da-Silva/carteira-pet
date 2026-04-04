import sqlite3, os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(50), senha VARCHAR(250),
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP)''')

c.execute('''CREATE TABLE IF NOT EXISTS tutor (
    id_tutor INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor VARCHAR(100), email VARCHAR(100),
    celular VARCHAR(20), telefone VARCHAR(20),
    logradouro VARCHAR(50), numero_logradouro VARCHAR(10),
    complemento VARCHAR(20), bairro VARCHAR(50),
    cidade VARCHAR(50), uf VARCHAR(2), cep VARCHAR(9),
    usuario_id INTEGER NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuario (id_usuario))''')

c.execute('''CREATE TABLE IF NOT EXISTS especie (
    id_especie INTEGER PRIMARY KEY AUTOINCREMENT,
    especie VARCHAR(50))''')

c.execute('''CREATE TABLE IF NOT EXISTS veterinario (
    id_veterinario INTEGER PRIMARY KEY AUTOINCREMENT,
    veterinario VARCHAR(100), email VARCHAR(100),
    celular VARCHAR(16), telefone VARCHAR(16),
    logradouro VARCHAR(50), numero_endereco VARCHAR(10),
    bairro VARCHAR(50), cidade VARCHAR(50),
    uf VARCHAR(2), cep VARCHAR(9),
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP)''')

c.execute('''CREATE TABLE IF NOT EXISTS pet (
    id_pet INTEGER PRIMARY KEY AUTOINCREMENT,
    pet VARCHAR(50), raca VARCHAR(50), sexo VARCHAR(1),
    data_nascimento DATE, castrado VARCHAR(1), data_castracao DATE,
    tutor_id INTEGER NOT NULL, especie_id INTEGER NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tutor_id) REFERENCES tutor (id_tutor),
    FOREIGN KEY (especie_id) REFERENCES especie (id_especie))''')

c.execute('''CREATE TABLE IF NOT EXISTS pet_veterinario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id_pet_id INTEGER NOT NULL,
    veterinarian_id_veterinario_id INTEGER NOT NULL,
    FOREIGN KEY (pet_id_pet_id) REFERENCES pet (id_pet),
    FOREIGN KEY (veterinarian_id_veterinario_id) REFERENCES veterinario (id_veterinario),
    UNIQUE(pet_id_pet_id, veterinarian_id_veterinario_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS vacina (
    id_vacina INTEGER PRIMARY KEY AUTOINCREMENT,
    vacina VARCHAR(70), obs_vacina VARCHAR(200),
    data_aplicacao DATE NOT NULL,
    pet_id INTEGER NOT NULL, veterinarian_id INTEGER NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pet_id) REFERENCES pet (id_pet),
    FOREIGN KEY (veterinarian_id) REFERENCES veterinarian (id_veterinario))''')

c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Canina')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Felina')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Ave')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Roedor')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Reptil')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Equina')")
c.execute("INSERT OR IGNORE INTO especie (especie) VALUES ('Outros')")

conn.commit()
conn.close()
print('Tabelas criadas com sucesso!')