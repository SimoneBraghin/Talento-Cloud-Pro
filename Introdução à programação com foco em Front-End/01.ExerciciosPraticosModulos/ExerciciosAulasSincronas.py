# Exercício Regar a planta:
"""
Este arquivo consiste nas atividades desenvolvidas durante as aulas síncronas, sendo então propostas coletivas, 
não apenas de autoria da criadora deste repositório
"""


"""
i = 0
while i <= 5:
    print("Robôzin, por favor regue a planta de número " + str(i))
    i += 1
"""
# Pedir para o robô regar apenas as plantas de números pares, sendo o intervalo de 0 a 5:
"""
i = 0

while i <= 5:
    if i % 2 == 0:
        print("Robôzin, por favor regue a planta de número " + str(i))
        i += 1
"""

# Criar uma função que peça ao usuário um número entre 0 e 100 até que um valor válido seja recebido
# Acrescentar a restrição de que o número inserido seja par
# Acrescentar a restrição de que o número inserido seja divisível por 3
"""
def pedirNumero():
    valorUsuario = False
    while not valorUsuario:
        respostaUsuario = input("Escreva um número entre 0 a 100: ")
        numeroUser = int(respostaUsuario)
        if numeroUser > 100:
            print("O número deve ser menor ou igual a 100")
        elif numeroUser < 0:
            print("O número deve ser maior ou igual a zero")
        elif numeroUser % 2 != 0:
            print("Você digitou um número ímpar. O número deve ser par")
        elif numeroUser % 3 != 0:
            print("O número deve ser divisível por 3")
        else:
          print("Obrigada pelo preenchimento! O número " + respostaUsuario + " é um valor válido")
          valorUsuario = True

pedirNumero()
"""

# Exercício de exemplo da aula:
"""
numeroCorreto = False

while (numeroCorreto == False):
   print("Insira um número par")
   try:
       numero = int(input())
       if (numero%2 == 0):
           numeroCorreto = True
           print("Você digitou um numero par !")
       else :
           print("Você digitou um número impar")
   except:
       print("Caracter inválido, por favor digite um número par")
"""

# 08/01

# Escreva uma função que verifica se array contém dado elemento

"""def verificarElemento(array, elemento):
    return elemento in array

elemento_existe = verificarElemento([1,2,3,4,5,6], "hello")
print(elemento_existe)

# Adicionar o índice a uma mensagem retornarda caso o elemento esteja no array
def verificarComMensagem(array, elemento):
    for i in range(13):
        print(i)
        

mensagem = verificarComMensagem([1,2,3,4,7,100,343,1234],33)
print(mensagem)
"""

# Escreva uma função que verifica se tem dado em determinado elementos + Encontrar Index do array
 
"""def VerifyElement(arr, element):
  exitentElement = element in arr
  if exitentElement:
    return "O elemento: "+ str(element) + " está no Índice: "  + str(arr.index(element))
  else:
    return "Elemento " + str(element) + " não encontrado no Array!"

retorno = VerifyElement([2, 4, 6, 8, 10], 6)
print(retorno)"""

"""def verificar_elemento(lista, elemento):
    if elemento in lista:
        indice = lista.index(elemento)
        return f"O elemento {elemento} está na posição {indice} da lista."
    else:
        return f"O elemento {elemento} não está na lista."
 
minha_lista = [30, 33, 36, 39, 42]
elemento_verificar = 30
 
mensagem = verificar_elemento(minha_lista, elemento_verificar)
print(mensagem)"""

"""def verificarValor(arr, elemento):
    for i in range(len(arr)):
        if arr[i] == elemento:
            return "O elemento está na posição " + str(i)
    return "Não encontrado"

retorno = verificarValor(["Mary Poppins", "My Fairy Lady", "Noviça Rebelde", "Funny Girl"], "Mary Poppins")
print(retorno)"""


#desafio pedir um valor do usuário até que o elemento fornecido esteja no array
"""elementoNoArray = False

idades = [14,16,17,33,78]

while elementoNoArray == False:
    valorUser = int(input("Inform um valor numérico: "))
    pertenceArray = verifica(idades, valorUser)

    if pertenceArray:
        elementoNoArray = True
        print("O valor está no array!")
    else:
        print("O valor não está no array, tente novamente!")
"""

# 
"1"+ 2