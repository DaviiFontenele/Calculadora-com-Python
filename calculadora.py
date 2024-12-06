# calculadora com while


"""
aqui esta a calculadora com python

ira funcionar quando entrar no terminal

ou so clicar em "ctrl + j"

"""

#codigo:


# solicitei a tag while e nela fiz as variaveis com os inputs para iniciar a calculadora


# essas primeiras linhas solicitam o numero e o operador, e validam
while True:
    numero_1 = input("Digite um Número: ")
    numero_2 = input("Digite outro Número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None  #estou validando os numeros
    num_1_float = 0
    num_2_float = 0
    
    # aqui na try crio variaveis e transformo em float
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    # se for colocado outro caracteres que sao sejam numeros dara esse if e ira voltar para o começo do codigo com a tag "continue"
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


    # aqui e a calculadora, poderia utilizar somente essas linhas, porem preciso fazer as validações para nao dar erro no codigo

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
