# SINTAXE BUILT-IN
## Sintaxe das quatro built-in data types em Python: (1) Listas, (2) Tuplas, (3) Conjuntos e (4) Dicionários
________________________________________________________
### LISTAS
    
    Listas são indexadores e, por isso, permitem modificação dos valores e também a duplicação de valores:
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    Listas são ordenadas, logo, a ordem dos valores internos da lista não podem ser modificados

    Para criar listas no Python é necessário:

    1. Utilizar o símbolo [] (colchetes) para as listas
    2. Armazenar a lista em uma VARIÁVEL
    3. Separar itens da lista pela vírgula

    EXEMPLO DE CÓDIGO:

        lista_compras = ['banana','laranja','maçã']
        print(lista_compras)
        ['banana', 'laranja', 'maçã']

#### Alterando Listas:
        
        # Acessando os índices:
            lista_frutas = ['maçã', 'banana', 'pera']
            print(lista_frutas)
            # Imprimirá: ['maçã', 'banana', 'pera']

            lista_frutas[0] = 'melancia'
            print(lista_frutas)
            # Imprimirá: ['melancia', 'banana', 'pera']
            
        # Alterando dados usando índices:
            # exemplo 1
            lista_frutas = ['melancia', 'banana', 'pera']
            print(lista_frutas)
            # Imprimirá: ['melancia', 'banana', 'pera']

            lista_frutas[1], lista_frutas[2] = 'morango', 'abacaxi'
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi']

            # exemplo 2
            lista_frutas = ['melancia', 'morango', 'abacaxi']
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi']

            lista_frutas[1] = lista_frutas[0]
            print(lista_frutas)
            # Imprimirá: ['melancia', 'melancia', 'abacaxi']

#### Adicionar e remover elementos da lista:

            # Adicionando:
            lista_frutas = ['melancia', 'morango', 'abacaxi']
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi']

            lista_frutas.append('kiwi')
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']

            # Removendo:
            lista_frutas = ['melancia', 'morango', 'abacaxi', 'kiwi']
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']

            lista_frutas.pop()
            print(lista_frutas)
            # Imprimirá: ['melancia', 'morango', 'abacaxi']
________________________________________________________
### ARRAYS (VETORES/MATRIZES)

    Array é uma variável especial que pode conter mais de um valor ao mesmo tempo.
    Exemplo:
            car1 = "Ford"
            car2 = "Volvo"
            car3 = "BMW"

    O Python não tem suporte built-in para Arrays (matrizes). Mas, essas podem ser utilizadas a partir de Listas.
    
    EXEMPLO DE CÓDIGO:

        cars = ["Ford", "Volvo", "BMW"]
        x = cars[0]
        cars[0] = "Toyota"

    Podemos ter um array de arrays:
        array_arrays = [[1,2,3], ['a', 'b', 'c']]

    É possível criar arrays mistos:
        array_misto = [10, "dez", True]

    
#### Percorrer Arrays
        
        lista_frutas = ['maçã', 'banana', 'pera']

         for i in range(3):
            print(lista_frutas[i])

        # Imprimirá:
        # maçã
        # banana
        # pera
             A função range pode receber até três argumentos que representam: 
             o valor inicial do contador, 
             a condição de parada, 
             o incremento do contador. 
             Se, ao invés de passarmos os três valores, passarmos apenas um valor como argumento, 
             ele representará a condição de parada. 
             No exemplo acima, a condição de parada é 3, em outras palavras, que o contador seja menor que 3 (i < 3).
             Como não passamos mais argumentos, a função range() atribui um valor
             padrão para o valor inicial e o incremento do contador. Estes valores por padrão são 0 e +1, respectivamente.
            
            Dessa forma, ao usar a função range(3) os elementos para nossa estrutura de repetição ficam assim:

            - Valor inicial do contador = 0
            - Condição de parada = contador < 3
            - Incremento do contador = 1

            Na primeira volta do loop, o contador (representado pela variável ‘i’) tem valor 0. 
            Por esse motivo, se imprimirmos lista_frutas[i] estamos dizendo na verdade lista_frutas[0] 
            e o valor impresso é ‘maçã’. Ainda nessa volta, aplicamos o incremento, que neste caso é 1, 
            por tanto o contador tem agora o valor 1.

        
        Quando não sabemos o tamanho da lista e não temos como contá-la por ser muito extensa, podemos usar o len():

        lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
        
        for i in range(len(lista_num)):
            print(lista_num[i])
________________________________________________________
### TUPLAS

    Tuplas são usadas para armazenar múltiplos itens em uma única variável; 
    é uma coleção onde a ordem dos valores é imutável;
    são escritas com o uso do parênteses.

    São ordenadas, imutáveis e permitem duplicata de valores. Ademais, são indexadas [0] a [n]

    EXEMPLO DE CÓDIGO:
        mytuple = ("apple", "banana", "cherry", "apple", "cherry")
________________________________________________________
### CONJUNTOS

    São usados para armazenar múltiplos itens em uma variável singular;
    são desordenadas, imutáveis e não indexáveis; não permite duplicação de valores

    EXEMPLO DE CÓDIGO:
        thisset = {"apple", "banana", "cherry"}
        print(thisset)
________________________________________________________
### DICIONÁRIOS 
    São usadas para armazenar dados em chaveamento com valores pares (key:value pair) 
        que podem ser utilizados pela referência(chamada) do nome da chave
    São ordenados, mutáveis, não permitem valoers duplicados
    

    EXEMPLO DE CÓDIGO:
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        print(thisdict["brand"])

________________________________________________________
### Referências:

    - Official documentation for Python 3.10.8. 
        Disponível em: https://docs.python.org/pt-br/3.7/library/array.html. Acesso em: 12 de out. 2022

    - KITAMURA, Celso. O Que É Array Em Python? 
        Disponível em: https://www.youtube.com/watch?v=1QlG_XiED0g. Acesso em 12 de out. 2022

    - SHERRILL, Derrick. Python Algorithm Series. 
        Disponível em: https://www.youtube.com/playlist?list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv. Acesso em 12 de out. 2022

    - FelixTechTips. Merge Sort In Python Explained (With Example And Code). 
        Disponível em: https://www.youtube.com/watch?v=cVZMah9kEjI. Acesso em 12 de out. 2022

    - Official documentation for Python 3.10.8. 
        Disponível em: https://docs.python.org/pt-br/3.7/library/array.html. Acesso em: 12 de out. 2022

    - KITAMURA, Celso. O Que É Array Em Python? 
        Disponível em: https://www.youtube.com/watch?v=1QlG_XiED0g. Acesso em 12 de out. 2022

    - SHERRILL, Derrick. Python Algorithm Series. 
        Disponível em: https://www.youtube.com/playlist?list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv. Acesso em 12 de out. 2022

    - FelixTechTips. Merge Sort In Python Explained (With Example And Code). 
        Disponível em: https://www.youtube.com/watch?v=cVZMah9kEjI. Acesso em 12 de out. 2022

    - Official documentation for Python 3.10.8. 
        Disponível em: https://docs.python.org/pt-br/3.7/library/array.html. Acesso em: 12 de out. 2022

    - KITAMURA, Celso. O Que É Array Em Python? 
        Disponível em: https://www.youtube.com/watch?v=1QlG_XiED0g. Acesso em 12 de out. 2022

    - SHERRILL, Derrick. Python Algorithm Series. 
        Disponível em: https://www.youtube.com/playlist?list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv. Acesso em 12 de out. 2022

- [FelixTechTips. Merge Sort In Python Explained (With Example And Code)](https://www.youtube.com/watch?v=cVZMah9kEjI) Acesso em 12 de out. 2022
    
- [Aprendendo sobre vetores](https://www.youtube.com/watch?v=7yBXNGVyN3Q)
