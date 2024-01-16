# ÍNDICES E CUMPRIMENTOS
___________________________________
## Índices (index)
    Index é o valor inteiro que representa cada um dos valores do array/lista 
    e que começa sempre do número 9 e vai iterando +1

        lista_frutas = ['maçã', 'banana', 'pera']
        print(lista_frutas[0])
        
        # Imprimirá: 'maçã'

    Acessar o item do array/lista usando o método descrito não elimina o item do array/lista 
    ou o alteraria de qualquer forma. Só o estamos chamando para visualização ou uso específico. 
    Veja o exemplo:

        lista_frutas = ['maçã', 'banana', 'pera']
        fruta_preferida = lista_frutas[2]

        print(fruta_preferida)
        print(lista_frutas)

        # O primeiro print() imprimirá: 'pera'
        # O segundo print() imprimirá: ['maçã', 'banana', 'pera']

___________________________________
## Cumprimento | len()
    
    O cumprimento é um recurso que facilita o processo de conhecimento do tamanho da listas/arrays, i. e., o número de itens. 
    Isso se faz importante porque há listas com número imenso de itens.

    Iniciando o contador em "1", porque o len() trás o valor referente a soma dos elementos da lista,
    ao contrário do índice que se inicia em "0" por padrão no python

    A função len() (do inglês, *length* ) nos permite saber o número de itens dentro de uma lista/array, 
    como segue exemplo:

        lista_frutas = ['maçã', 'banana', 'pera']
        quantidade_frutas = len(lista_frutas)

        print(quantidade_frutas)

        # Imprimirá o número 3, pois lista_frutas tem três elementos


    O len() pode também servir como argumento da função print() ser ser guardada previamente em uma variável.
    Exemplo: 

        lista_frutas = ['maçã', 'banana', 'pera']
        print(len(lista_frutas))
        # Também imprimirá o número 3

___________________________________
## Referências:
    - Official documentation for Python 3.10.8. 
        Disponível em: https://docs.python.org/pt-br/3.7/library/array.html. Acesso em: 12 de out. 2022

    - KITAMURA, Celso. O Que É Array Em Python? 
        Disponível em: https://www.youtube.com/watch?v=1QlG_XiED0g. Acesso em 12 de out. 2022

    - SHERRILL, Derrick. Python Algorithm Series. 
        Disponível em: https://www.youtube.com/playlist?list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv. Acesso em 12 de out. 2022

    - FelixTechTips. Merge Sort In Python Explained (With Example And Code). 
        Disponível em: https://www.youtube.com/watch?v=cVZMah9kEjI. Acesso em 12 de out. 2022