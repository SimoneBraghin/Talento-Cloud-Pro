# Escopos de Variáveis

Escopo é a parte de dentro da variável. 
Exemplo: uma função (def()) é uma variável e seu escopo é local.

- Variáveis declaradas dentro de uma função não podem ser acessadas fora dela. Neste caso, dizemos que a variável é local porque ela só existe dentro de seu escopo - limintando a pela função onde é declarada  

- Variáveis declaradas fora de qualquer função são chamadas de globais. Elas estão no escopo acessível a todas as funções. Uma aplicação costumas de variáveis globais é o armazenamento de valores constantes.  
    Exemplo:  

        bebida = "refri"  
        
        def cardapio():  
            comida = "sanduba"  
            bebida = "suco"
            print(bebida) # dentro da função = suco
        
        cardapio()
        print(bebida) # fora da função tbm será = refri

- É possível alterar variáveis locais dentro de funções (escopos locais). Para isso, indicamos a função que queremos alterar a variável global. Mas, a alteração dela será local, apenas dentro da função local. Caso queira alterar a global dentro da função a estrutura deverá chamar a global dentro da função.  
    Exemplo:  
      
        bebida = "refri"  
        
        def cardapio():  
            global bebida  
            comida = "sanduba"  
            bebida = "suco"
            print(bebida) # dentro da função = suco
        
        cardapio()
        print(bebida) # fora da função tbm será = suco
