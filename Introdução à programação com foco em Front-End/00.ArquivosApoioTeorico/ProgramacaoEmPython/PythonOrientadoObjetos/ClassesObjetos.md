 # Programação Orientada a Objetos (POO)
 Programação orientada a objetos (POO) é um paradigma da progrmaação que pensa a modelagem de dados e comportamentos como se esses fossem objetos do mundo real.

 Objetos em python são a representação de um objeto do mundo real. Objetos tem dois componentes:
 1. Propriedades:  
 Exemplo: ligado/desligado; volume max./ volum mínimo, etc.
 2. Comportamentos:  
 Exemplo: mudar de canal; aumentar/diminuir volume; liga/desligar equipamentos, etc.

 Temos que modelar o mundo de modo a alterar diversas funções do mesmo objeto, conforme tipos de componentes que ele possua.

 POO é mais límpo, conciso e legibilidade, por meio de **classes, heranças, encapsulamento, abstrações e polimorfismos**

 ## Classes
 São as palavras-chaves que definem o que um objeto irá ser. Ela não é o objeto.  Ela define as características e comportamentos de um objeto. Não conseguimos usar a classe diretamente. 
 
 Uma classe pode ter diversos objetos (múltiplas instâncias) que são, por sua vez, objetos distintos e autoconditos.  
 **Classes possuem nomes no singular.** 

 Toda classe tem dentro dela um método (chamado construtor) Este método construtor serve para inicializar o objeto da classe com seus valores padrão.

### A diferença entre função [def()] e método é que:
1. O método é associado a uma classe e atua sobre um objeto
2. O primeiro parâmetro do método é chamado de *self* e representa a instância sobre a qual o método atuará. Ele é a instância especial de atributos que pode ser acessado por qualquer método dentro da classe.
![Classe e Método](/Introdução%20à%20programação%20com%20foco%20em%20Front-End/00.ArquivosApoioTeorico/ProgramacaoEmPython/PythonOrientadoObjetos/imagens/Classe.Metodo.png)  

Na chamada do método não é necessário passar o parâmetro *self*. Contudo, não podemos deixar de declarar na construção do parâmetro o *self* como primeiro parâmetro dos métodos. Por ser atributo especial, ele não muda ou se encerra com o uso de outras funções dentro da classe. Por isso ele é tão especial.


## Objetos

Os objetos, ao contrário, podem ser usados e possuem características e comprotamentos definidos nas classes.