from classes import Autor
from validacao import getInt

def menu_autores(biblioteca):
    while True:
        print("\n------ Gestão de Autores ------")
        print("1 - Adicionar Autor")
        print("2 - Listar Autores")
        print("0 - Voltar ao Menu Principal")
        print("------------------------------")

        escolha = getInt("opção")
    
        if escolha == 1:
            try:
                nome_completo = input("Introduza o nome do autor: ")
                data_nasc = input("Introduza a data de nascimento do autor (dd-mm-aaaa): ")
                email = input("Introduza o email do autor: ")

                autor = biblioteca.adicionar_autor(nome_completo, data_nasc, email)
                print(autor)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif escolha == 2:
            try:
                biblioteca.listar_autores()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif escolha == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
