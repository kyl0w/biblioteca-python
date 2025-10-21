from validacao import getInt

def menu_livros(biblioteca):
    while True:
        print("\n------ Gestão de Livros ------")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Listar Livros")
        print("4 - Levantar Livro")
        print("5 - Devolver Livro")
        print("5 - Devolver Livro")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("opção")

        # If's encadeados para escolher a opção do utilizador
        if escolha == 1:
            try: 
                titulo = input("Introduza o titulo: ")
                # Criar uma lista vazia para armazenar os autores
                nova_lista_autor = []
                # ciclo while para ler os autores ate que o utilizador saia
                while True:
                    novo_autor = input("Introduza um novo autor ou 's' para terminar: ")
                    if novo_autor.lower() == 's':
                        # Sai do ciclo se o utilizador 
                        break
                    else: 
                        # adiciona um novo autor à nossa lista
                        nova_lista_autor.append(novo_autor) # O nossos nossos autores têm que existir na base de dados
                
                editora = input("Introduza o nome da editora: ") # o nome da editora tem que exister na nossa base de dados
                palavraChave = input("Introduza a palavra chave: ") # a palavra chave tem que ser única
                ano = getInt("ano") # Chama a função getInt para validar ler os dados e validar o inteiro

                # Adicionar um novo livro à biblioteca
                biblioteca.adicionar_livro(titulo=titulo, lista_autor=nova_lista_autor, nome_editora=editora, palavraChave=palavraChave, ano=ano)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif escolha == 2:
            biblioteca.ler_livros()
        elif escolha == 3:
            try:
                palavraChave = input("Introduza a palavra chave: ")
                biblioteca.consultar_livro()
            except Exception as e:
                print(e)
        elif escolha == 4:
            try:
                nome_utilizador = input("Introduza o seu nome de utilizador: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                palavra_chave = input("Introduza a palavra-chave do livro: ")
                
                biblioteca.levantar_livro(nome_utilizador, palavra_chave)
            except Exception as e:
                print(f"Ocorreu um erro {e}: ")
        elif escolha == 5:
            biblioteca.devolver_livro()
        elif escolha == 0:
            break
        else:
            print("Opção inválida")