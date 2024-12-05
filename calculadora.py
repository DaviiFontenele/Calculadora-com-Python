# calculadora com while


"""
Esse campo sera usado para novas tags:

.lower = transforma tudo que for maiusculo em minusculo.

.startwith = começa com.

"""

#codigo:

while True:
    numero_1 = input("Digite um Número: ")
    numero_2 = input("Digite outro Número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos os numeros nao são validos.")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("operador invalido")
        continue

    if len(operador) > 1:
        print("digite apenas um operador.")
        continue

    print("realizando sua conta, confira abaixo: ")

    if operador == "+":
        print(f"{numero_1}+{num_2_float}=", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{numero_1}-{num_2_float}=", num_1_float - num_2_float)
    elif operador == "/":
        print(f"{numero_1}/{num_2_float}=", num_1_float / num_2_float)
    elif operador == "*":
        print(f"{numero_1}*{num_2_float}=", num_1_float * num_2_float)
    else:
        print("deu erro, escreva direito")


#sair da calculadora
    sair = input("Quer Sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
