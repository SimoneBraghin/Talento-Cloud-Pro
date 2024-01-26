________________________________________________________
# FUNÇÕES:
## Sintaxe
### EXPLICACAO 1:
        
        def nome_da_funcao(parametro1, parametro2, ...):
            # Corpo da função
            # Pode conter várias linhas de código
            # Pode usar os parâmetros passados à função
            
            # Retorno opcional
            return resultado


        - def: É a palavra-chave utilizada para definir uma função.

        - nome_da_funcao: É o nome que você escolhe para sua função. 
            Siga as convenções de nomenclatura do Python (letras minúsculas com underscores para separar palavras, se necessário).

        - (parametro1, parametro2, ...): São os parâmetros que a função pode receber. 
            Esses são opcionais. Você pode ter zero ou mais parâmetros.

        - return: Esta palavra-chave é usada para retornar um valor da função. O return é opcional. 
            Se não houver um return explícito ou se a função não contiver um return, ela retornará None.

        
        EXEMPLOS:

        Exemplo de função simples que soma dois números:
            def soma(a, b):
                resultado = a + b
                return resultado


        Você pode chamar essa função passando os argumentos e atribuir o resultado a uma variável:
            resultado_soma = soma(3, 5)
            print(resultado_soma)  # Saída: 8

### EXPLICACAO 2:

        def nome_da_funcao(argumento1, argumento2, ...):
        """Docstring da função"""
        # Corpo da função
        # Aqui você escreve o código que a função executará
        # Pode conter várias linhas de código
        # Pode incluir estruturas de controle (if, for, while, etc.)
        # Pode realizar operações, cálculos, etc.
        
        # Opcionalmente, a função pode retornar um valor
        return algum_valor

        ## Explicação dos elementos:

                def: É a palavra-chave utilizada para iniciar a definição de uma função.
                nome_da_funcao: É o nome que você escolhe para sua função. Deve seguir as mesmas regras de nomenclatura de variáveis em Python.
                (argumento1, argumento2, ...): São os argumentos (parâmetros) que a função pode receber. Estes são opcionais e você pode ter zero ou mais argumentos separados por vírgula. Eles são utilizados para passar informações para a função.
                """Docstring da função""": É uma string de documentação (docstring) opcional que descreve o propósito da função. Ajuda a documentar o que a função faz.
                Corpo da função: É onde o código real da função é escrito. Ele deve estar indentado para delimitar o bloco de código pertencente à função.
                return algum_valor: É uma declaração opcional que permite à função retornar um valor após sua execução. Esta instrução é usada para sair da função e pode retornar um valor específico de volta para onde a função foi chamada.
                Aqui está um exemplo simples de uma função que retorna a soma de dois números:

        # EXEMPLO FUNÇÃO:

                def soma(a, b):
                    """Esta função retorna a soma de dois números."""
                    resultado = a + b
                    return resultado
________________________________________________________
Referências:

- [BRANDÃO, Leônidas. Introdução ao uso de funções](https://www.ime.usp.br/~leo/mac2166/2017-1/introducao_funcoes.html#:~:text=A%20ideia%20básica%20de%20uma,e%20posterior%20invocação%20à%20função) Instituto de Matemática e Estatística Universidade de São Paulo, [s/d]. Acesso em: 04 abr. 2022.