
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

___________________________________
Referências:

- [GATTO, Elaine. Tratamento de erros. 52 slides. Universidade Sagrado Coração, 19 nov. 2013](https://pt.slideshare.net/elainececiliagatto/tratamento-de-erros) Acesso em: 6 abr. 2022.

    PYTHON. Erros e Exceções. [s/d]. 
        Disponível em: https://docs.python.org/pt-br/3/tutorial/errors.html. Acesso em: 6 abr. 2022. 

    W3SCHOOL.Python Try Except. [s/d]. 
        Disponível em: https://www.w3schools.com/python/python_try_except.asp. Acesso em: 6 abr. 2022.

    SIQUEIRA, Fernando. Tratamento de Erros e Exceções. Prof. Fernando de Siqueira, [s/d]. 
        Disponível em: https://sites.google.com/site/proffernandodesiqueira/disciplinas/paradigmas-de-linguagens-de-programacao/aula-6---tratamento-de-erros-e-excecoes. Acesso em: 6 abr. 2022.