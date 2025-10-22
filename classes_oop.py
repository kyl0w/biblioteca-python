# 
# Este ficheiro apenas guarda o código antes da implementação de um sistema de base de dados
#


import re

# Verificao da segurança da password
def verificar_password(password):

    if len(password) < 8: return False

    if not re.search(r"[a-z]", password): return False

    if not re.search(r"[A-Z]", password): return False

    if not re.search(r"\d", password): return False

    if not re.search(r"[@$!%*?&.,:]", password): return False

    return True

class Pessoa:
    def __init__(self, nomeCompleto, dataDeNascimento, email):
        if not isinstance(nomeCompleto, str) or not nomeCompleto.strip():
            raise ValueError("Nome completo inválido")
        if not isinstance(dataDeNascimento, str) or not dataDeNascimento.strip():
            raise ValueError("Data de nascimento inválida")
        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email inválido")
        
        self.__nomeCompleto = nomeCompleto
        self.__dataDeNascimento = dataDeNascimento
        self.__email = email

    def get_nome(self):
        return self.__nomeCompleto   
    
    def get_dataDeNascimento(self):
        return self.__dataDeNascimento   
    
    def get_email(self):
        return self.__email   
         
class Autor(Pessoa): 
    def __init__(self, nomeCompleto, dataDeNascimento, email):
        #chamar os atributos da classe pessoa
        super().__init__(nomeCompleto, dataDeNascimento, email)
        self.__livros_publicados = []
        
    def get_livros_publicados(self):
        return self.__livros_publicados
            
        
class Utilizador(Pessoa):
    def __init__(self, numero, nome, password, nomeCompleto, dataDeNascimento, email):
        super().__init__(nomeCompleto, dataDeNascimento, email)
        
        if not isinstance(numero, str) or not numero:
            raise ValueError("Número inválido")
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome de utilizador inválido")
        if not isinstance(password, str) or not verificar_password(password):
            raise ValueError("Password inválida")

        self.__numero = numero
        self.__nome = nome
        self.__password = password

    def get_utilizador_nome(self):
        return self.__nome
    
    def get_password(self, password):
        if password == self.__password:
            return True
        return False
    
    def adicionar_emprestimos(self, livro):
        self.__historicoEmprestimos.append(livro)
    
    def entregar_livro(self, livro):
        # Remove um livro do histórico de empréstimos se existir
        if livro in self.__historicoEmprestimos:
            self.__historicoEmprestimos.remove(livro)
            return True
        return False

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
             Nome Completo: {super().get_nome()}
             Data de Nascimento: {super().get_dataDeNascimento()}
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

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_morada(self, morada):
        self.__morada = morada

    def set_contacto(self, contacto):
        self.__contacto = contacto

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
            # Verifica se a variavel palavra chave é igual à palavra chave armazena na classe Livro correspondente
            if palavraChave == livro.get_palavraChave(): 
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
    
    def levantar_livro(self, nome, palavra_chave):
        
        # Cria uma variável para armazenar o utilizador
        utilizador = None

        # Irá percorrer a lista de utilizadores
        for u in self.__listaUtilizadores:
            # Sai do ciclo quando encontra o utilizador
            if u.get_utilizador_nome() == nome:
                utilizador = u
                break
        # Caso não encontre nenhum utilizador dá erro
        if not utilizador:
            raise Exception("Utilizador não encontrado")
        
        livro = None
        for l in self.__listaLivros:
            if l.get_palavraChave() == palavra_chave:
                livro = l
        if not livro:
            raise Exception("Livro não encontrado.")
        if not livro.get_disponivel():
            raise Exception("Livro não disponivel.")
        
        livro.levantar_livro()
        utilizador.adicionar_emprestimos(livro)
        return f"-> O livro {livro.get_titulo()} foi levantado por {utilizador.get_nome()}"

    def devolver_livro(self, nome, palavraChave):
        # Procurar utilizador que está a efetuar a devolucao
        utilizador = self.pesquisar_utilizador(nome=nome)
        # Caso não encontre um utilizador através do seu nome lança uma exceção
        if not utilizador:
            raise Exception("Utilizador não encontrado")
        
        # Irá pesquisar o livro pelo nome ou palavra-chave
        for l in self.__listaLivros:
            # Caso encontre um livro válido
            if l.get_nome() == nome or l.get_palavraChave() == palavraChave:
                l.entregar_livro()
                utilizador.entregar_livro(l)
                return "Livro entregue com sucesso" 
        
        raise Exception("Livro não encontrado")
    
    def listar_emprestimos(self, nome):
        for utilizador in self.__listaUtilizadores:
            utilizador.get_historico()

    #
    # --------- Utilizadores ----------
    #

    def adicionar_utilizadores(self, nomeCompleto, nome, numero, password, dataNascimento, email):
        self.__listaUtilizadores.append(
            Utilizador(
                nome=nome, 
                numero=numero,
                password=password,
                dataDeNascimento=dataNascimento, 
                nomeCompleto=nomeCompleto,
                email=email
            )
        )

        return "Utilizador criardo com sucesso"
        
        
    def listar_utilizadores(self):
        for utilizador in self.__listaUtilizadores:
            utilizador.get_utilizador()

    # Método para pesquisar um utilizador através de vários campos opcionais
    def pesquisar_utilizador(self, nome=None, email=None):
        for i in self.__listaUtilizadores:
            if nome:
                if i.get_nome() == nome:
                    return i
            if email:
                if i.get_email() == email:
                    return i
        return 

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