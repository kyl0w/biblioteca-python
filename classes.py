"""
Pretende-se desenvolver um sistema de gestão de biblioteca em Python, utilizando
os princípios da Programação Orientada a Objetos (POO). O sistema deve permitir a
gestão de livros, editoras, autores e utilizadores. O foco está na criação de uma
arquitetura bem estruturada com múltiplas classes, herança e interação entre
objetos. Opcionalmente, os dados podem ser armazenados de forma persistente
numa base de dados PostgreSQL.

"""

class Pessoa:
    def __init__(self, nomeCompleto, dataDeNascimento, email):
        self.__nomeCompleto = nomeCompleto
        self.__dataDeNascimento = dataDeNascimento
        self.__email = email

    def getPessoa(self):
        print(f"Nome: {self.__nomeCompleto}\nData de nascimento: {self.__dataDeNascimento}\nEmail: {self.__email}")

    def get_nome(self):
        return self.__nomeCompleto   
         
class Autor(Pessoa): 
    def __init__(self, nomeCompleto, dataDeNascimento, email):
        #chamar os atributos da classe pessoa
        super().__init__(nomeCompleto, dataDeNascimento, email)
        self.__livros_publicados = []
        
    def get_livros_publicados(self):
        return self.__livros_publicados
            
        
class Utilizador(Pessoa):
    def __init__(self, numero, nome, username, password, nomeCompleto, dataDeNascimento, email):
        super().__init__(nomeCompleto=nomeCompleto, dataDeNascimento=dataDeNascimento, email=email)
        self.__numero = numero
        self.__nome = nome
        self.__username = username
        self.__password = password
        
        self.__historicoEmprestimos = []
    
    def get_utilizador_nome(self):
        return self.__nome
    
    def adicionar_emprestimos(self, livro):
        self.__historicoEmprestimos.append(livro)
    
    # Método utilizado para devolver o histórico do utilizador
    def get_historico(self):
        # Verifica se existe algum livro emprestado ao utilizador
        if self.__historicoEmprestimos:
            print(f"O utilizador {self.__nome} levantou os seguintes livros: ")
            # A cada livro encontrado vai devolver o sue titulo
            for livro in self.__historicoEmprestimos:
                print(f" {livro.get_titulo()}")
        else:
            print(f"O utilizador {self.__nome} ainda não levantou livros ")
    
    def get_utilizador(self):
       print(f"""
             Nome: {self.__nome}
             Número: {self.__numero}
        """)
    
class Editora:
    def __init__(self, nome, morada, contacto):
        self.__nome = nome 
        self.__morada = morada
        self.__contacto = contacto

    def get_editora(self):
        print(f"""
            Nome: {self.__nome}
            Morada: {self.__morada}
            Contacto: {self.__contacto}
        """)

    # Método para alterara editora, inicia com os valores como nulos
    def alterar_editora(self, nome=None, morada=None, contacto=None):
        # Se o campo nome vier com valor, efetua a alteração caso não, procede
        if nome:
            self.set_nome(nome)
        
        # Se o campo morada vier com valor, efetua a alteração caso não, procede
        if morada:
            self.set_morada(morada)

        # Se o campo morada vier com valor, efetua a alteração caso não, procede
        if contacto:
            self.set_contacto(contacto)

        return "-> Editora alterada com sucesso"

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_morada(self, morada):
        self.__morada = morada

    def set_contacto(self, contacto):
        self.__contacto = contacto
        
class Livro:
    # campo ISBN para ter um identificador unico
    def __init__(self, titulo, listaAutor, editora, palavraChave, ano):
        self.__titulo = titulo
        self.__listaAutor = listaAutor
        self.__editora = editora # a editora tem que ser do tipo Editora
        self.__palavraChave = palavraChave
        self.__ano = ano      
        self.__disponivel = True  
    
    def get_disponivel(self):
        return self.__disponivel
    
    def get_titulo(self):
        return self.__titulo
    
    # Método para devolver todos os dados do livro
    def get_livro(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Editora: {self.__editora}")
        print(f"Autores: {self.__listaAutor}")
        print(f"Palavra Chave: {self.__palavraChave}")
        print(f"Ano: {self.__ano}")
        print(f"Disponivel: {self.__disponivel}")

    def get_palavraChave(self):
        return self.__palavraChave # Vai devolver o atributo do tipo str palavraChave

    def get_lista_autor(self):
        pass

    # 
    def levantar_livro(self):
        self.__disponivel = False

    def entregar_livro(self):
        self.__disponivel = True

class Biblioteca:
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__listaLivros = []
        self.__listaUtilizadores = []
        self.__listaEditoras = []
        self.__listaAutores = []

    #
    # --------- Livros ----------
    #

    # Função para listar todos os livros
    def ler_livros(self):
        # vai percorrer a list de livros 
        for livro in self.__listaLivros: # [Livro, livro, livro]
            livro.get_livro()# vai assumir um objeto Livro da lista e aceder ao seu método

    # Funcao para consultar apenas um livro
    def consultar_livro(self, palavraChave):
        for livro in self.__listaLivros:
            if palavraChave == livro.get_palavraChave(): # Verifica se a variavel palavra chave é igual à palavra chave armazena na classe Livro correspondente
                livro.get_livro()
                
    # Função para criar livros
    def adicionar_livro(self, titulo, lista_autor, nome_editora, palavraChave, ano):
        # Vai pesquisar a editora pelo nome, se não existir não cria o livro
        editora = self.get_editora(nome=nome_editora)
        if not editora:
            raise Exception("Editora não existe")

        for autor in lista_autor:
            if not self.get_autor(nome=autor):
                raise Exception("Autor(s), introduzidos não são válidos")
        
        # Vai adicionar à nossa listaLivros um objeto do Livro com os dados que foram enviados
        livro = self.__listaLivros.append(
            Livro(
                titulo=titulo,
                listaAutor=lista_autor, # do tipo list['nome_autor']
                editora=editora, # editora é do tipo Editora
                palavraChave=palavraChave,
                ano=ano
            )
        )
        
        if livro:
            return "Livro criado com sucesso"
        else:
            return False
    
    def levantar_livro(self, nome_utilizador, palavra_chave):
       
        utilizador = None

        for u in self.__listaUtilizadores:
            if u.get_utilizador_nome() == nome_utilizador:
                utilizador = u
                break
        if not utilizador:
            raise Exception("Utilizador não encontrado")
            return
        
        livro = None
        for l in self.__listaLivros:
            if l.get_palavraChave() == palavra_chave:
                livro = l
        if not livro:
            raise Exception("Livro não encontrado.")
            return
        if not livro.get_disponivel():
            raise Exception("Livro não disponivel.")
            return
        
        livro.levantar_livro()
        utilizador.adicionar_emprestimos(livro)
        return f"-> O livro {livro.get_titulo()} foi levantado por {nome_utilizador}"
        
        

    def devolver_livro(self):
        pass
    
    #
    # --------- Utilizadores ----------
    #

    def adicionar_utilizadores(self, nome, numero, password, username):
        try:
            self.__listaUtilizadores.append(
                Utilizador(
                    nome=nome,
                    numero=numero,
                    password=password,
                    username=username
                )
            )

            return "-> Utilizador criado com sucesso"
        
        except Exception as e:
            return f"Ocorreu um erro: {e}"
        
    def listar_utilizadores(self):
        for utilizador in self.__listaUtilizadores:
            utilizador.get_utilizador()

    #
    # --------- Autores ----------
    #
         
    def adicionar_autor(self, nome, data_nasc, email):
        self.__listaAutores.append(
            Autor(
                nomeCompleto=nome,
                dataDeNascimento=data_nasc,
                email=email
            )
        )

        return "Autor criado com sucesso"

    def listar_autores(self):
        for autor in self.__listaAutores:
            autor.get_nome()

    # Pesquisa autor pelo nome ou pelo email
    def get_autor(self, nome=None, email=None):
        if nome:
            for autor in self.__listaAutores:
                if autor.get_nome() == nome:
                    return True
        elif email:
            for autor in self.__listaAutores:
                if autor.get_email() == email:
                    return True
        return False

    #
    # --------- Editoras ----------
    #

    def adicionar_editora(self, nome, morada, contacto):
        self.__listaEditoras.append(
            Editora(
                nome=nome,
                morada=morada,
                contacto=contacto
            )
        )

        return "-> Editora criada com sucesso"
    
    def listar_editoras(self):
        for editora in self.__listaEditoras:
            editora.get_editora()

    # Vai buscar a editora através do nome
    def get_editora(self, nome=None):
        for editora in self.__listaEditoras:
            # vai buscar o nome da editora atual no ciclo
            nome_editora = editora.get_nome()
            if nome_editora == nome:
                # retorna um instancia de Editora
                return editora
        return