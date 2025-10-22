from validacao import getInt
from utilizadores import login
from datetime import datetime

def menu_livros(biblioteca):
    while True:
        print("\n------ Gestão de Livros ------")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Pesquisar Livro")
        print("4 - Levantar Livro")
        print("5 - Devolver Livro")
        print("6 - Lista Emprestimos")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("opção")

        if escolha == 1:
            try:
                titulo = input("Introduza o título: ")
                nova_lista_autor = []
                while True:
                    novo_autor = getInt("ID do autor (0 para sair)")
                    if novo_autor == 0:
                        break
                    nova_lista_autor.append(novo_autor)

                editora_id = getInt("ID da editora")
                palavra_chave = input("Introduza a palavra-chave (única): ")
                ano = getInt("Ano")
                isbn = input("Introduza o ISBN: ")

                resultado = biblioteca.adicionar_livro(
                    titulo=titulo,
                    lista_autor=nova_lista_autor,
                    editora_id=editora_id,
                    palavra_chave=palavra_chave,
                    ano=ano,
                    isbn=isbn
                )
                print(resultado)

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif escolha == 2:
            livros = biblioteca.ler_livros()
            if livros:
                for livro in livros:
                    print(f"ID: {livro['id']}, Título: {livro['titulo']}, "
                          f"Palavra-chave: {livro['palavra_chave']}, Ano: {livro['ano']}, "
                          f"ISBN: {livro['isbn']}, Editora: {livro['nome_editora']}")
            else:
                print("Nenhum livro registado.")

        elif escolha == 3:
            try:
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                livro = biblioteca.consultar_livro(palavra_chave)
                print(f"Título: {livro['titulo']}, Editora: {livro['nome_editora']}, "
                      f"Ano: {livro['ano']}, ISBN: {livro['isbn']}")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == 4:
            try:
                nome = input("Nome de utilizador: ")
                password = input("Password: ")
                palavra_chave = input("Palavra-chave do livro: ")

                # Login do utilizador
                try:
                    login(nome, password, biblioteca)
                    resultado = biblioteca.levantar_livro(nome, palavra_chave)
                    print(resultado)
                except Exception as e:
                    print(f"Ocorre erro: {e}")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif escolha == 5:
            try:
                nome = input("Nome de utilizador: ")
                password = input("Password: ")
                livro_nome = input("Nome do livro a devolver (vazio se não souber): ")
                palavra_chave = input("Palavra-chave do livro (vazio se não souber): ")

                if login(nome, password, biblioteca):
                    resultado = biblioteca.devolver_livro(nome, livro_nome, palavra_chave)
                    print(resultado)
                else:
                    print("Login inválido.")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif escolha == 6:
            try:
                nome = input("Nome de utilizador para ver empréstimos: ")
                biblioteca.listar_emprestimos(nome)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif escolha == 0:
            break

        else:
            print("Opção inválida")
