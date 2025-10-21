from classes import Autor
    
def menu_autores(biblioteca):
    while True:
        print("\n------ Gestão de Livros ------")
        print("1 - Adicionar Editora")
        print("2 - Listar Editoras")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = input("Escolha uma opção: ")

    
        # If's encadeados para escolher a opção do utilizador
        if escolha == 1:
            try:
                nome = input("Introduza o nome da editora: ") # O nome tem que ser único
                morada = input("Introduza a morada  da editora: ")
                contacto = input("Introduza o contacto da editora: ")

                novaEditora = biblioteca.adicionar_editora(nome=nome, morada=morada, contacto=contacto)
                print(novaEditora)
            except Exception as e:
                print("Ocorreu um erro: {e}")
        elif escolha == 2:
            biblioteca.listar_editoras()
        else:
            break