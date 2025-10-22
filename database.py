import sqlite3

# Ligação à base de dados
try:
    conn = sqlite3.connect('biblioteca.db')
    # ativa a ligação com chaves estrangeiras, nã é ativado por default no SQLite
    conn.row_factory = sqlite3.Row
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
        nome_completo TEXT NOT NULL,
        data_nasc TEXT,
        email TEXT UNIQUE
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Autor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pessoa INTEGER NOT NULL UNIQUE,
        FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id) ON DELETE CASCADE
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Utilizador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE,
        id_pessoa INTEGER NOT NULL UNIQUE,
        numero TEXT UNIQUE,
        password TEXT,
        FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id) ON DELETE CASCADE
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
        editora_id INTEGER NOT NULL,
        palavra_chave TEXT,
        ano INTEGER,
        isbn TEXT UNIQUE NOT NULL,
        FOREIGN KEY (editora_id) REFERENCES Editora(id) ON DELETE SET NULL
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS LivroAutor (
        livro_id INTEGER,
        autor_id INTEGER,
        PRIMARY KEY (livro_id, autor_id),
        FOREIGN KEY (livro_id) REFERENCES Livro(id) ON DELETE CASCADE,
        FOREIGN KEY (autor_id) REFERENCES Autor(id) ON DELETE CASCADE
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS HistoricoEmprestimo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        utilizador_id INTEGER,
        data_levantamento TEXT,
        data_devolucao TEXT,
        FOREIGN KEY (livro_id) REFERENCES Livro(id) ON DELETE CASCADE,
        FOREIGN KEY (utilizador_id) REFERENCES Utilizador(id) ON DELETE CASCADE
    );
    """
]

# Execução de todas as querys
for sql in tabelas:
    cursor.execute(sql)

# Guardar alterações e fechar conexão
conn.commit()

print("Base de dados SQLite 'biblioteca.db' criada com sucesso!")