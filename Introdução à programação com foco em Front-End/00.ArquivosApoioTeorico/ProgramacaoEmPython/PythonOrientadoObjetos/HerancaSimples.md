# Herança Simples

Herança é uma ferramenta que permite o reuso do código em classes diferentes.  

A Herança permite adicionar novas funcionalidades sem modificar uma classe existente - criando uma classe filha (derivada).  

A Herança funciona de modo transitivo: a classe B herda as funcionalidades da classe A, todas que herdaram da classe B irão herdar da classe A.  

- Para testar se um objeto é de instância de determinada classe:  
    print("TEXTO", isinstance(nomeObjeto, nomeClasse))

- Teste entre Classes:
    print("TEXTO", issubclass(nomeClassePai, nomeClasseHerdeira))
