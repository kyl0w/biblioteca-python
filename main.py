# TPC 4
# Tiago Lourenço 146128-B / thlourenco@emfa.gov.pt
# Thomas Bergereau 146131-B / tjbergereau@emfa.gov.pt

import re
import connect
import os
from classes import Biblioteca
from utilizadores import menu_utilizadores
from livros import menu_livros
from editoras import menu_editoras
from autores import menu_autores
from validacao import getInt

biblioteca = Biblioteca(titulo="Minha Biblioteca")


# Função principal do nosso código
def main():
    
    # Começar um ciclo infinito até que o utilizador decida sair
    while True:
        # Menu a ser apresentado ao utilizador

        print("\n---------- Menu Principal ----------")
        print("1 - Livros")
        print("2 - Utilizadores")
        print("3 - Autores")
        print("4 - Editoras")
        print("6 - Sair")
        print("------------------------------------")

        
        escolha = getInt("escolha") # Irá chamar a função getInt para ser Introduzido um número válido
        os.system('cls')

        if escolha == 1:
            menu_livros(biblioteca)
        elif escolha == 2:
            menu_utilizadores(biblioteca)
        elif escolha == 3:
            menu_autores(biblioteca)
        elif escolha == 4:
            menu_editoras(biblioteca)
        elif escolha == 6:
            print("A sair... Até breve!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()