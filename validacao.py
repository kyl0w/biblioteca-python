from datetime import datetime
import re

# Função utilizada para validar inteiros
def getInt(s):
    while True:
        try:
            n  = int(input(f"Introduza o(a) {s}: "))
            return n
        except Exception as e:
            print("Introduza um número válido")

# Função para validar as datas
def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    

# Verificao da segurança da password
def verificar_password(password):

    if len(password) < 8: return False

    if not re.search(r"[a-z]", password): return False

    if not re.search(r"[A-Z]", password): return False

    if not re.search(r"\d", password): return False

    if not re.search(r"[@$!%*?&.,:]", password): return False

    return True

def validar_string(valor, nome_campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{nome_campo} inválido")

def validar_email(email):
    validar_string(email, "Email")
    if not re.match(r"^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w+$", email):
        raise ValueError("Formato de email inválido")
