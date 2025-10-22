from validacao import getInt

def menu_editoras(biblioteca):
    while True:
        print("\n------ Gestão de Editoras ------")
        print("1 - Adicionar Editora")
        print("2 - Listar Editoras")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("Escolha")

        if escolha == 1:
            try:
                nome = input("Introduza o nome da editora: ")
                morada = input("Introduza a morada da editora: ")
                contacto = input("Introduza o contacto da editora: ")

                resultado = biblioteca.adicionar_editora(nome=nome, morada=morada, contacto=contacto)
                print(resultado)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif escolha == 2:
            try:
                editoras = biblioteca.listar_editoras()
                if editoras:
                    for e in editoras:
                        print(f"ID: {e['id']}, Nome: {e['nome']}, Morada: {e['morada']}, Contacto: {e['contacto']}")
                else:
                    print("Nenhuma editora registada.")
            except Exception as e:
                print(f"Ocorreu um erro ao listar editoras: {e}")

        elif escolha == 0:
            break
        else:
            print("Opção inválida")
