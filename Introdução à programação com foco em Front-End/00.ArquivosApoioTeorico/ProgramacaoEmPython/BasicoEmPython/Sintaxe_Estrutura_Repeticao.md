# ESTRUTURAS DE REPETIÇÃO
___________________________________
### WHILE

    while condição:
        # Bloco de código a ser executado enquanto a condição for verdadeira
        # Pode conter várias linhas de código
        # É importante atualizar a variável da condição para evitar loops infinitos

    ## Explicação dos elementos:

        while: É a palavra-chave utilizada para iniciar a estrutura de repetição.
        condição: É a expressão booleana que determina se o bloco de código associado ao while será executado. Enquanto essa condição for verdadeira, o bloco de código dentro do while será repetidamente executado. Se a condição se tornar falsa, a execução do loop while é interrompida e o controle passa para o código após o bloco while.
        Bloco de código: É o conjunto de instruções que será executado repetidamente enquanto a condição for verdadeira. Esse bloco de código deve estar indentado corretamente para indicar que faz parte do loop while.
        É importante tomar cuidado ao utilizar a estrutura de repetição while, já que se a condição nunca se tornar falsa, isso resultará em um "loop infinito", onde o código continuará a ser executado indefinidamente.

        Aqui está um exemplo simples de um loop while que conta até 5:

    # EXEMPLO WHILE:  
       
        contador = 1

        while contador <= 5:
            print(contador)
            contador += 1  # Atualiza o contador para avançar para o próximo número

___________________________________
### DO-WHILE
    Em Python, não existe uma estrutura de controle nativa chamada "do-while" como encontrada em algumas outras linguagens de programação, como C, C++, Java, entre outras. No entanto, é possível simular um comportamento semelhante ao "do-while" utilizando a estrutura while em conjunto com uma variável de controle.

    A ideia por trás de um loop "do-while" é executar um bloco de código pelo menos uma vez e, em seguida, repeti-lo enquanto a condição é verdadeira. Em Python, você pode conseguir algo semelhante dessa forma:

    # EXEMPLO DO-WHILE:

    primeira_vez = True

    while True:
        # Código que deve ser executado pelo menos uma vez
        if primeira_vez:
            # Bloco de código que é executado na primeira iteração
            print("Isso será executado pelo menos uma vez.")
            primeira_vez = False
        
        # Condição que determina a continuação ou interrupção do loop
        # Aqui você coloca a condição que deveria ser verificada após a primeira execução
        # Se a condição for atendida, o loop é interrompido
        if not condição:
            break
        
        # Restante do código que é executado enquanto a condição for verdadeira
        # ...


    ## Explicação dos elementos:

        Neste exemplo, a variável primeira_vez é usada para garantir que o código dentro do bloco if primeira_vez: seja executado pelo menos uma vez. Após a primeira execução desse bloco, primeira_vez é atualizado para False para evitar que o mesmo bloco seja executado novamente nas iterações subsequentes.

        Depois disso, a condição que normalmente seria verificada no início do loop "do-while" é testada no final do loop while True. Se a condição for atendida, o loop continua; caso contrário, break é usado para sair do loop.

        Essa é uma abordagem comum para simular um comportamento "do-while" em Python, já que não existe uma estrutura nativa dedicada para isso.

___________________________________
### FOR
    
    Um loop for é usado para iterar sobre uma sequência 
    (como uma lista, tupla, dicionário, conjunto ou string) ou um iterável. 
    A estrutura básica de um loop for em Python é a seguinte:

        for elemento in sequencia_ou_iteravel:
        # Faça algo com o elemento
        # Aqui dentro você pode realizar operações com o elemento atual do loop

        Aqui está um exemplo simples de como você pode usar um loop for para percorrer uma lista:
           
            # Definindo uma lista
            lista = [1, 2, 3, 4, 5]

            # Iterando sobre a lista com um loop for
            for elemento in lista:
            print(elemento)  # Isso imprimirá cada elemento da lista

        Você também pode usar a função *range()* 
        para gerar uma sequência de números em um intervalo e iterar sobre ela usando um loop for:

            # Usando range() para gerar uma sequência de números de 0 a 4
            for i in range(5):
            print(i)  # Isso imprimirá os números de 0 a 4

        Além disso, você pode usar o for em dicionários para percorrer chaves, valores ou ambos:

            # Definindo um dicionário
            dicionario = {'a': 1, 'b': 2, 'c': 3}

            # Iterando sobre as chaves do dicionário
            for chave in dicionario:
                print(chave)  # Isso imprimirá cada chave do dicionário

            # Iterando sobre os valores do dicionário
            for valor in dicionario.values():
                print(valor)  # Isso imprimirá cada valor do dicionário

            # Iterando sobre chaves e valores simultaneamente
            for chave, valor in dicionario.items():
                print(f'Chave: {chave}, Valor: {valor}')  # Isso imprimirá chave e valor juntos



___________________________________
## Referências:

- [APOIO INFORMÁTICA. Comandos de repetição.[S.d.]]( https://www.apoioinformatica.inf.br/produtos/item/14-comandos-de-repeticao) Acesso em: 26 abr. 2022.

    AZEVEDO, Adriano. Estruturas de repetição. GitHub, 10 ago. 2018. 
        Disponível em: https://github.com/drianoaz/visualg/blob/master/docs/04-estruturas-de-repeticao.md .Acesso em: 26 abr. 2022.

    CURSO EM VÍDEO.Estruturas de Repetição 1 - Curso de Algoritmos #09 - Gustavo Guanabara. 26 maio 2014. 
        Disponível em: https://www.youtube.com/watch?v=U5PnCt58Q68 . Acesso em: 26 abr. 2022.
    
    CURSO EM VÍDEO.Estruturas de Repetição 3 - Curso de Algoritmos #11 - Gustavo Guanabara. 2 jun. 2014. 
        Disponível em: https://www.youtube.com/watch?v=fP49L1i_-HU . Acesso em: 26 abr. 2022.
    
    CURSO EM VÍDEO.Estruturas de Repetição 2 - Curso de Algoritmos #10 - Gustavo Guanabara. 9 jun. 2014. 
        Disponível em: https://www.youtube.com/watch?v=WJQz20i7CyI. Acesso em: 26 abr. 2022.

    ALVES, Gustavo. Estrutura de repetição ENQUANTO. Dicas de Programação, [s.d.]. 
        Disponível em: https://dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto/. Acesso em: 26 abr. 2022.
    
    ALVES, Gustavo. Estrutura de repetição REPITA-ATÉ. Dicas de Programação, [s.d.]. 
        Disponível em: https://dicasdeprogramacao.com.br/estrutura-de-repeticao-repita-ate/. Acesso em: 26 abr. 2022.
    
    ALVES, Gustavo. Estrutura de repetição PARA. Dicas de Programação, [s.d.]. 
        Disponível em: https://dicasdeprogramacao.com.br/estrutura-de-repeticao-para/. Acesso em: 26 abr. 2022.

    ALVES, William Pereira. Linguagem e lógica de programação. 1º edição. São Paulo: Érica, 2014.
    
    FORBELLONE, André Luiz Villar. Lógica de programação: A construção de algoritmos e estruturas de dados. 3º edição. São Paulo: Pearson Prentice Hall, 2005.
    
    REIS, Fábio. Lógica de Programação – Estrutura de Repetição REPITA ATÉ – 14. Bóson Treinamentos em Ciência e Tecnologia, 9 jun. 2013. 
        Disponível em: http://www.bosontreinamentos.com.br/logica-de-programacao/logica-de-programacao-estruturas-de-repeticao-loop-repita-ate-14/. Acesso em: 26 abr. 2022.

    REIS, Fábio. Lógica de Programação – Estrutura de Repetição PARA – 15. Bóson Treinamentos em Ciência e Tecnologia, 9 jun. 2013. 
        Disponível em: http://www.bosontreinamentos.com.br/logica-de-programacao/15-logica-de-programacao-estruturas-de-repeticao-loop-para/ . Acesso em: 26 abr. 2022.

    MARIANO, Diego. Laços de Reptição. Diego Mariano, 28 ago. 2020. 
        Disponível em: https://diegomariano.com/lacos-de-repeticao-2/. Acesso em: 31 mar. 2022.

    HASHTAG. ESTRUTURAS DE REPETIÇÃO NO PYTHON. Hashtag, 21 jun. 2021. 
        Disponível em: https://www.hashtagtreinamentos.com/estruturas-de-repeticao-python?gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGgOgorf-KWfc6jqxkpn7c8Qu2DktSGEj51bMjeZbOTKn93fLmPAkGgaAjnlEALw_wcB. Acesso em: 31 mar. 2022.

    HORN, Michelle. Python while: executar código com condição verdadeira!. Betrybe, [s/d]. 
        Disponível em: https://blog.betrybe.com/python/python-while/. Acesso em: 31 mar. 2022.
