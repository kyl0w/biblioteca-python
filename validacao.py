# Função utilizada para validar inteiros
def getInt(s):
    while True:
        try:
            n  = int(input(f"Introduza o(a) {s}: "))
            return n
        except Exception as e:
            print("Introduza um número válido")
