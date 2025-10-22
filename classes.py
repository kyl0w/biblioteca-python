"""
Pretende-se desenvolver um sistema de gestão de biblioteca em Python, utilizando
os princípios da Programação Orientada a Objetos (POO). O sistema deve permitir a
gestão de livros, editoras, autores e utilizadores. O foco está na criação de uma
arquitetura bem estruturada com múltiplas classes, herança e interação entre
objetos. Opcionalmente, os dados podem ser armazenados de forma persistente
numa base de dados PostgreSQL.

"""

import re
from database import conn, cursor
from validacao import validar_data, verificar_password 
from datetime import datetime



class Pessoa:
    def __init__(self, nome_completo, data_nasc, email):
        # Validação dos dados
        # Verificar se o Nome Completo é uma string e se existe
        if not isinstance(nome_completo, str) or not nome_completo:
            raise ValueError("Nome completo inválido")
        # Verificar se a data o é uma string, se existe e se tem um formato válido
        if not isinstance(data_nasc, str) or not data_nasc or not validar_data(data_nasc):
            raise ValueError("Data de nascimento inválida('dd-mm-aaaa')")
        # Verificar se a data o é uma string, se existe e se tem um formato válido
        if not isinstance(email, str) or not email:
            raise ValueError("Email inválido")
        if not re.match(r"^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w+$", email):
            raise ValueError("Formato de email inválido")
        
        # Verificar se o email já existe
        cursor.execute("SELECT id FROM Pessoa WHERE email = ?", (email,))
        # se o cursor encontrar alguma correspondecia lanca a excecao
        if cursor.fetchone():
            raise ValueError("Email já existe")
        
        self.__nome_completo = nome_completo
        self.__data_nasc = data_nasc
        self.__email = email
         
class Autor(Pessoa): 
    def __init__(self, nome_completo, data_nasc, email):
        #chamar os atributos da classe pessoa
        super().__init__(nome_completo, data_nasc, email)
        
        
class Utilizador(Pessoa):
    def __init__(self, numero, nome, password, nome_completo, data_nasc, email):
        super().__init__(nome_completo, data_nasc, email)
        
        if not isinstance(numero, int) or not numero:
            raise ValueError("Número inválido")
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome de utilizador inválido")
        if not isinstance(password, str) or not verificar_password(password):
            raise ValueError("Password inválida")

        self.__numero = numero
        self.__nome = nome
        self.__password = password
       
class Editora:
    def __init__(self, nome, morada, contacto):
        # Validação do nome
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome da editora inválido")
        # Validação da morada
        if not isinstance(morada, str) or not morada:
            raise ValueError("Morada da editora inválida")
        # Validação do contacto
        if not isinstance(contacto, str) or not contacto:
            raise ValueError("Contacto da editora inválido")
        # Verifica se já existe editora com o mesmo nome
        cursor.execute("SELECT id FROM Editora WHERE nome = ?", (nome,))
        if cursor.fetchone():
            raise Exception("Editora já existe")
        
        self.__nome = nome 
        self.__morada = morada
        self.__contacto = contacto
        
class Livro:
    # campo ISBN para ter um identificador unico
    def __init__(self, titulo, listaAutor, editora, palavra_chave, ano, isbn):
        self.__titulo = titulo
        self.__listaAutor = listaAutor
        self.__editora = editora # a editora tem que ser do tipo Editora
        self.__palavra_chave = palavra_chave
        self.__ano = ano      
        self.__isbn = isbn
        self.__disponivel = True  

    def levantar_livro(self):
        self.__disponivel = False

    def entregar_livro(self):
        self.__disponivel = True

class Biblioteca:
    def __init__(self, titulo):
        self.__titulo = titulo

    # --------- Livros ----------

    # Função para listar todos os livros
    def ler_livros(self):
        cursor.execute("""
            SELECT l.id, l.titulo, l.palavra_chave, l.ano, l.isbn, e.nome AS nome_editora
            FROM Livro l
            LEFT JOIN Editora e ON l.editora_id = e.id
        """)

        return cursor.fetchall()
    
    # Funcao para consultar apenas um livro
    def consultar_livro(self, palavra_chave):
        cursor.execute("""
            SELECT l.id, l.titulo, l.palavra_chave, l.ano, l.isbn,
                   e.nome AS nome_editora
            FROM Livro l
            LEFT JOIN Editora e ON l.editora_id = e.id
            WHERE l.palavra_chave = ?
        """, (palavra_chave,))
        livro = cursor.fetchone()

        if not livro: 
            raise(f"Nenhum livro encontrado com a palavra-chave '{palavra_chave}'.")
        
        return livro
        
    # Função para criar livros
    def adicionar_livro(self, titulo, lista_autor, editora_id, palavra_chave, ano, isbn):
        cursor.execute("SELECT id FROM Editora WHERE id = ?", (editora_id,))

        # Verifica se ISBN já existe
        cursor.execute("SELECT id FROM Livro WHERE isbn = ?", (isbn,))
        if cursor.fetchone():
            raise ValueError(f"ISBN '{isbn}' já está registado.")
        
        if not cursor.fetchone():
            raise ValueError("Editora não encontrada")

        for autor_id in lista_autor:
            cursor.execute("SELECT id FROM Autor WHERE id = ?", (autor_id,))
            if not cursor.fetchone():
                raise ValueError(f"Autor {autor_id} não encontrado")

        cursor.execute("INSERT INTO Livro (titulo, editora_id, palavra_chave, ano, isbn) VALUES (?, ?, ?, ?, ?)",
                       (titulo, editora_id, palavra_chave, ano, isbn))
        
        livro_id = cursor.lastrowid

        for autor_id in lista_autor:
            cursor.execute("INSERT INTO LivroAutor (livro_id, autor_id) VALUES (?, ?)", (livro_id, autor_id))
        conn.commit()

        return "Livro criado com sucesso!"
    
        
    def levantar_livro(self, nome_utilizador, palavra_chave):
        # Buscar utilizador
        cursor.execute("""
            SELECT U.id AS utilizador_id, P.nome_completo
            FROM Utilizador U
            JOIN Pessoa P ON U.id_pessoa = P.id
            WHERE U.nome = ?
        """, (nome_utilizador,))
        utilizador = cursor.fetchone()
        if not utilizador:
            raise Exception("Utilizador não encontrado")
        print("1")
        # Buscar livro
        cursor.execute("""
            SELECT L.id AS livro_id, L.titulo, L.disponivel
            FROM Livro L
            WHERE L.palavra_chave = ?
        """, (palavra_chave,))
        livro = cursor.fetchone()
        if not livro:
            raise Exception("Livro não encontrado")
        
        print("1")
        if livro['disponivel'] == 0:
            raise Exception("Livro não disponível")

        # Registrar empréstimo
        cursor.execute("""
            INSERT INTO HistoricoEmprestimo (livro_id, utilizador_id, data_levantamento)
            VALUES (?, ?, ?)
        """, (
            livro['livro_id'],
            utilizador['utilizador_id'],
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        ))
        
        print("1")
        # Atualizar disponibilidade do livro
        cursor.execute("UPDATE Livro SET disponivel = 0 WHERE id = ?", (livro['livro_id'],))
        conn.commit()
        
        print("1")
        return f"-> O livro '{livro['titulo']}' foi levantado por {utilizador['nome_completo']}"

    def devolver_livro(self, nome_utilizador, palavra_chave):
        # Buscar utilizador
        cursor.execute("""
            SELECT U.id AS utilizador_id, P.nome_completo
            FROM Utilizador U
            JOIN Pessoa P ON U.id_pessoa = P.id
            WHERE U.nome = ?
        """, (nome_utilizador,))
        utilizador = cursor.fetchone()
        if not utilizador:
            raise Exception("Utilizador não encontrado")

        # Buscar livro
        cursor.execute("""
            SELECT L.id AS livro_id, L.titulo
            FROM Livro L
            WHERE L.palavra_chave = ?
        """, (palavra_chave,))
        livro = cursor.fetchone()
        if not livro:
            raise Exception("Livro não encontrado")

        # Atualizar histórico de devolução
        cursor.execute("""
            UPDATE HistoricoEmprestimo
            SET data_devolucao = ?
            WHERE livro_id = ? AND utilizador_id = ? AND data_devolucao IS NULL
        """, (
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            livro['livro_id'],
            utilizador['utilizador_id']
        ))

        # Atualizar disponibilidade do livro
        cursor.execute("UPDATE Livro SET disponivel = 1 WHERE id = ?", (livro['livro_id'],))
        conn.commit()

        return f"-> O livro '{livro['titulo']}' foi devolvido por {utilizador['nome_completo']}"

    #
    # --------- Utilizadores ----------
    #

    def criar_utilizador(self, numero, nome, password, nome_completo, data_nasc, email):
        utilizador = Utilizador(numero, nome, password, nome_completo, data_nasc, email)
        cursor.execute("INSERT INTO Pessoa (nome_completo, data_nasc, email) VALUES (?, ?, ?)",
                       (nome_completo, data_nasc, email))
        pessoa_id = cursor.lastrowid
        cursor.execute("INSERT INTO Utilizador (id_pessoa, numero, nome, password) VALUES (?, ?, ?, ?)",
                       (pessoa_id, numero, nome, password))
        conn.commit()
        return f"Utilizador '{nome}' criado com sucesso."
        
        
    def listar_utilizadores(self, ):
        cursor.execute("""SELECT u.id, u.numero, u.nome, u.password, p.nome_completo, p.data_nasc, p.email
                          FROM Utilizador u JOIN Pessoa p ON u.id_pessoa = p.id""")
        return cursor.fetchall()

    def pesquisar_utilizador(self, nome=None, email=None):
        if nome:
            cursor.execute("""
                SELECT U.id AS utilizador_id,
                    U.numero,
                    U.nome,
                    P.nome_completo,
                    P.data_nasc,
                    P.email
                FROM Utilizador U
                JOIN Pessoa P ON U.id_pessoa = P.id
                WHERE U.nome = ?
            """, (nome,))
        elif email:
            cursor.execute("""
                SELECT U.id AS utilizador_id,
                    U.numero,
                    U.nome,
                    P.nome_completo,
                    P.data_nasc,
                    P.email
                FROM Utilizador U
                JOIN Pessoa P ON U.id_pessoa = P.id
                WHERE P.email = ?
            """, (email,))
        else:
            raise Exception("Necessário pelo menos um valor de pesquisa: nome ou email")

        utilizador = cursor.fetchone()

        if utilizador: return utilizador

        raise Exception("Utilizador não encontrado")

    # --------- Autores ----------
         
    def adicionar_autor(self, nome_completo, data_nasc, email):
        autor = Autor(nome_completo, data_nasc, email)
        cursor.execute("INSERT INTO Pessoa (nome_completo, data_nasc, email) VALUES (?, ?, ?)",
                       (nome_completo, data_nasc, email))
        pessoa_id = cursor.lastrowid
        cursor.execute("INSERT INTO Autor (id_pessoa) VALUES (?)", (pessoa_id,))
        conn.commit()
        return "Autor criado com sucesso."

    def listar_autores(self):
        cursor.execute("""SELECT A.id, P.nome_completo, P.data_nasc, P.email
                          FROM Autor A JOIN Pessoa P ON A.id_pessoa = P.id""")
        return cursor.fetchall()
    
    # --------- Editoras ----------

    def adicionar_editora(self, nome, morada, contacto):
        editora = Editora(nome, morada, contacto)
        cursor.execute("INSERT INTO Editora (nome, morada, contacto) VALUES (?, ?, ?)",
                       (nome, morada, contacto))
        conn.commit()
        return "Editora criada com sucesso."
    
    def listar_editoras(self):
        cursor.execute("SELECT id, nome, morada, contacto FROM Editora")
        return cursor.fetchall()