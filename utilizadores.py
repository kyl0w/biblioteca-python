import re
from validacao import getInt

# Verificar dados do utilizador
def login(nome, password, biblioteca):
    try:
        utilizador = biblioteca.pesquisar_utilizador(nome=nome)
        if not utilizador:
            raise Exception("Nome de utilizador inválido")
        if not utilizador["password"] != password:
            raise Exception("Password incorreta")
        return True
    except Exception as e:
        print(e)
    
def menu_utilizadores(biblioteca):
    while True:
        print("\n------ Gestão de Livros ------")
        print("1 - Adicionar Utilizador")
        print("2 - Listar Utilizadores")
        print("3 - Listar Emprestimos")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("opção")
        
        if escolha == 1:
            try:
                nome_completo = input("Introduza o seu nome completo: ")
                data_nasc = input("Introduza a sua data de nascimento: ")
                email = input("Introduza o seu email: ")
                nome = input("Introduza o seu nome: ")
                numero = getInt("numero")
                password = input("Introduza a sua palavra-passe: ")
                novo_utilizador = biblioteca.criar_utilizador(
                    nome_completo=nome_completo,
                    email=email,
                    data_nasc=data_nasc,
                    nome=nome, 
                    numero=numero, 
                    password=password,
                )
                print(novo_utilizador)
            except Exception as e:
                print(f"Ocorreu um erro ao criar utilizador: {e}")
        elif escolha == 2:
            try:
                utilizadores = biblioteca.listar_utilizadores()
                
                campos = ['id', 'numero', 'nome', 'password', 'nome_completo', 'data_nasc', 'email']

                # Transformar tuplas(formato da resposta do SQLite) em dicionários e imprimir
                # Ciclo pra percorrer os utilizadores devolvidos
                for u in utilizadores:
                    # neste for usamos o zip, que é uma função para combinar duas listas
                    for campo, valor in zip(campos, u):
                        # escreve os valores formatados
                        print(f"{campo}: {valor}")
                    # dá print de 40 "*""
                    print("-" * 40)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif escolha == 3:
            try:
                email = input("Introduza o seu email: ")
                nome = input("Introduza o seu nome: ")
                utilizador = biblioteca.pesquisar_utilizador(nome, email)
                # Transformar o resultado num dicionário
                campos = ["id", "numero", "nome", "nome_completo", "data_nasc", "email"]
                # neste for usamos o zip, que é uma função para combinar duas listas
                for campo, valor in zip(campos, u):
                    # escreve os valores formatados
                    print(f"{campo}: {valor}")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif escolha == 4:
            pass
        elif escolha == 0:
            break
        else:
            print("Opção inválida")