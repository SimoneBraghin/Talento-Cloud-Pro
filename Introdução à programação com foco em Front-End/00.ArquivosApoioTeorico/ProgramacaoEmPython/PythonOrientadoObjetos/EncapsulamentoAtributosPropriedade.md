# Encapsulamentos - Atributos e Propriedades

Para indicar ao usuário quais os atributos e métodos que não deverão ser alterados na classe, utiliza-se convenções (combinados).

Nome iniciados com "_" (underscore) são protegidos e não deve ser acessados pelo mundo externo a não ser que o usuário saiba o que está fazendo.

Nomes iniciados com "__" (underscore duplo) são privados e não devem ser acessados pelo mundo externo de modo algum.

## Atributos e Propriedades

**Não são sinônimos**

### Atributos
Todas as variáveis declaradas dentro de uma *classe* (que contém o self.nome_variável) são atributos.

### Propriedades
São o que nos dá acesso as variáveis que se parecem com atributos, mas na verdade usam métodos por trás dos panos.

Para declarar como propriedade, utiliza-se um "declarator", *@property* e a propriedade é o nome do método. Ela é uma variável privada. Esses métodos são chamados de "getter" porque retornar o valor da variável.

Para alterar um valor privado, utiliza-se o "declarator" *setter* junto com o nome do método e acima dele.