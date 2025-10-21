import sqlite3

# Ligação à base de dados
try:
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Ligação à base de dados estabelecida.")
except sqlite3.Error as e:
    print("Erro ao conectar à base de dados:", e)
    exit(1)

# Criação das tabelas
tabelas = [
    """
    CREATE TABLE IF NOT EXISTS Pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeCompleto TEXT NOT NULL,
        dataDeNascimento TEXT,
        email TEXT UNIQUE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Autor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pessoa INTEGER NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Utilizador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pessoa INTEGER NOT NULL,
        numero TEXT UNIQUE,
        FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Editora (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        morada TEXT,
        contacto TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        editora_id INTEGER,
        palavraChave TEXT,
        ano INTEGER,
        isbn TEXT UNIQUE,
        FOREIGN KEY (editora_id) REFERENCES Editora(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS LivroAutor (
        livro_id INTEGER,
        autor_id INTEGER,
        PRIMARY KEY (livro_id, autor_id),
        FOREIGN KEY (livro_id) REFERENCES Livro(id),
        FOREIGN KEY (autor_id) REFERENCES Autor(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS HistoricoEmprestimo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        utilizador_id INTEGER,
        dataLevantamento TEXT,
        dataDevolucao TEXT,
        FOREIGN KEY (livro_id) REFERENCES Livro(id),
        FOREIGN KEY (utilizador_id) REFERENCES Utilizador(id)
    );
    """
]


# Execução de todas as querys
for sql in tabelas:
    cursor.execute(sql)

# Guardar alterações
conn.commit()
conn.close()

print("Base de dados SQLite 'biblioteca.db' criada com sucesso!")