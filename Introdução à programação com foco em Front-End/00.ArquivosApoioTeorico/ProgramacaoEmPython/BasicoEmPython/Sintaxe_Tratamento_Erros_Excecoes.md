
Em Python, o tratamento de erros e exceções é feito usando blocos try, except, else e finally. 

___________________________________
### Try & Except:
   
    try:
        # Código onde uma exceção pode ocorrer
        # Se ocorrer uma exceção, o fluxo do programa será desviado para o bloco except
        # Se nenhuma exceção ocorrer, o bloco except será ignorado
    except ExcecaoTipo as nome_da_excecao:
        # Código para lidar com a exceção do tipo ExcecaoTipo
        # O código dentro deste bloco será executado se ocorrer uma exceção do tipo ExcecaoTipo

___________________________________
### Try, Except & Else:

    try:
        # Código onde uma exceção pode ocorrer
    except ExcecaoTipo as nome_da_excecao:
        # Código para lidar com a exceção do tipo ExcecaoTipo
    else:
        # Código a ser executado se NENHUMA exceção for lançada no bloco try

___________________________________
### Try, Except & Finally:

    try:
        # Código onde uma exceção pode ocorrer
    except ExcecaoTipo as nome_da_excecao:
        # Código para lidar com a exceção do tipo ExcecaoTipo
    finally:
        # Código que será executado sempre, independente de ter ocorrido exceção ou não

__________________________________

## Erros e Exceções

Existem dois tipos de erros:
- Erros de sintaxes
- Erros de exceções

### Erros de sintaxe
Erro na escrita do código

### Erros de exceção
Dar-se-á na lógica de execução linha a linha

__________________________________

#### SyntaxError:  
Ocorre quando há um erro de sintaxe no código.

    Exemplo de SyntaxError
    print("Olá, Mundo!'
    IndentationError: Ocorre quando há problemas com a indentação do código.

#### IndentationError:  
Ocorre quando há problemas com a indentação do código.

    Exemplo de IndentationError
    if True:
    print("Indentação incorreta")

#### NameError:  
Ocorre quando um nome de variável ou função não é encontrado.

    Exemplo de NameError
    print(variavel_inexistente)
    TypeError: Ocorre quando há uma operação aplicada a um tipo de dado incompatível.

#### TypeError:  
Ocorre quando há uma operação aplicada a um tipo de dado incompatível.

    Exemplo de TypeError
    soma = "10" + 5
    IndexError: Ocorre quando você tenta acessar um índice inválido em uma lista ou sequência.

#### IndexError:   
Ocorre quando você tenta acessar um índice inválido em uma lista ou sequência.

    Exemplo de IndexError
    lista = [1, 2, 3]
    elemento = lista[10]
    ValueError: Ocorre quando uma função recebe um argumento do tipo correto, mas com um valor incorreto.

#### ValueError:  
Ocorre quando uma função recebe um argumento do tipo correto, mas com um valor incorreto.

    Exemplo de ValueError
    numero = int("abc")
    KeyError: Ocorre ao tentar acessar uma chave inexistente em um dicionário.

#### KeyError:  
Ocorre ao tentar acessar uma chave inexistente em um dicionário.

    Exemplo de KeyError
    dicionario = {'a': 1, 'b': 2}
    valor = dicionario['c']
    FileNotFoundError: Ocorre quando um arquivo não é encontrado durante operações de leitura ou escrita.

#### FileNotFoundError:  
Ocorre quando um arquivo não é encontrado durante operações de leitura ou escrita.

    Exemplo de FileNotFoundError
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()

___________________________________
### Referências:

[GATTO, Elaine. Tratamento de erros. 52 slides. Universidade Sagrado Coração, 19 nov. 2013](https://pt.slideshare.net/elainececiliagatto/tratamento-de-erros) Acesso em: 6 abr. 2022.

[PYTHON. Erros e Exceções](https://docs.python.org/pt-br/3/tutorial/errors.html) Acesso em: 6 abr. 2022. 

[W3SCHOOL.Python Try Except](https://www.w3schools.com/python/python_try_except.asp) Acesso em: 6 abr. 2022.

[SIQUEIRA, Fernando. Tratamento de Erros e Exceções](https://sites.google.com/site/proffernandodesiqueira/disciplinas/paradigmas-de-linguagens-de-programacao/aula-6---tratamento-de-erros-e-excecoes) Acesso em: 6 abr. 2022.