import re
from validacao import getInt

# Verificao da segurança da password
def verificar_password(password):


    if len(password) < 8:
        raise Exception("A palavra passe tem que ter 8 caracteres")

    if not re.search(r"[a-z]", password):
        raise Exception("A password tem que ter uma minuscula")

    if not re.search(r"[A-Z]", password):
        raise Exception("A password tem que ter uma maiuscula")

    if not re.search(r"\d", password):
        raise Exception("A password tem que ter um numero")

    if not re.search(r"[@$!%*?&.,:]", password):
        raise Exception("A password tem que ter um caracter especial")

    print("Palavra passe válida.")
    return True

# Verificar dados do utilizador
def login(username, password, biblioteca):
    utilizador = biblioteca.get_utilizador(username=username)

    try:
        if not utilizador:
            raise Exception("Nome de utilizador inválido")
        if not utilizador.get_password(password):
            raise Exception("Password incorreta")
        return True
    except Exception as e:
        print(e)
        return False
    
def menu_utilizadores(biblioteca):
    while True:
        print("\n------ Gestão de Livros ------")
        print("1 - Adicionar Utilizador")
        print("2 - Listar Utilizadores")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("opção")
        
        if escolha == 1:
            try:
                nome = input("Introduza o seu nome: ")
                numero = getInt("numero")
                username = input("Introduza o seu username: ")
                password = input("Introduza a sua palavra: ")
                verificar_password(password)
                biblioteca.adicionar_utilizadores(nome=nome, numero=numero, username=username, password=password)
            except Exception as e:
                print(f"Ocorreu um erro ao criar utilizador: {e}")
        elif escolha == 6:
            break
        else:
            print("Opção inválida")