# Match Case

def verificar_tipo(dado):
    match dado:
        case str():
            print("É uma string")
        case int():
            print("É um número inteiro")
        case float():
            print("É um número decimal")
        case _:
            print("Tipo não reconhecido")

verificar_tipo(10)  # Saída: É um número inteiro
verificar_tipo("Olá")  # Saída: É uma string
verificar_tipo(3.14)  # Saída: É um número decimal
verificar_tipo(True)  # Saída: Tipo não reconhecido


___________________________________
Neste exemplo:

match dado: 
    é a estrutura principal onde a variável dado será testada em relação aos diferentes padrões.
case str(): 
    verifica se dado é uma string.
case int(): 
    verifica se dado é um número inteiro.
case float():  
    verifica se dado é um número decimal.
case _:
    o "_" é um curinga que corresponde a qualquer valor. Neste caso, ele é usado como um padrão 
        para qualquer outro tipo de dado não especificado nas condições anteriores.

Dentro de cada case, você pode adicionar código para ser executado se o padrão correspondido for encontrado.

Lembre-se de que o match case é uma ótima ferramenta para lidar com múltiplos casos de correspondência de padrões 
        e é útil para tornar o código mais legível e conciso.


__________________________________


def verificar_tipo(dado):
    match dado:
        case str(valor):
            print(f"É uma string: '{valor}'")
        case int(valor) if valor > 0:
            print(f"É um número inteiro positivo: {valor}")
        case int(valor) if valor < 0:
            print(f"É um número inteiro negativo: {valor}")
        case int():
            print("É um número inteiro zero")
        case float():
            print(f"É um número decimal: {dado}")
        case list(itens) if len(itens) > 0:
            print(f"É uma lista não vazia: {itens}")
        case list():
            print("É uma lista vazia")
        case _:
            print("Tipo não reconhecido")

verificar_tipo("Olá")               # Saída: É uma string: 'Olá'
verificar_tipo(10)                  # Saída: É um número inteiro positivo: 10
verificar_tipo(-5)                  # Saída: É um número inteiro negativo: -5
verificar_tipo(0)                   # Saída: É um número inteiro zero
verificar_tipo(3.14)                # Saída: É um número decimal: 3.14
verificar_tipo([1, 2, 3])           # Saída: É uma lista não vazia: [1, 2, 3]
verificar_tipo([])                  # Saída: É uma lista vazia
verificar_tipo(True)                # Saída: Tipo não reconhecido