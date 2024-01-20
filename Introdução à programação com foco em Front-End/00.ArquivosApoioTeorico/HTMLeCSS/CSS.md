# CSS (Cascading Style Sheets ou Folhas de Estilo em Cascata)

## Sobre o CSS
Lançada em 1996 pelo W3C, CSS foi idealizado por Hakon Wium Lie e Bert Bos em 1994.  
A partir do CSS versão 3.0 temos a modularização das especificações, não necessitando de nova versão, e maiores possibilidades de estilização.

## Formas de utilização do CSS
### Forma inline
<head>
    <title>Forma de utilizar o CSS</title>
</head>
<body>
    <h2>Forma de utilizar o CSS</h2>
    <p style="color: blue;">Essa é a forma inline.</p>
</body>

### Forma interna
<head>
    <title>Forma de utilizar o CSS</title>
    <style>
        p {
            color: red;
        }
    </style>
</head>
<body>
    <h2>Forma de utilizar o CSS</h2>
    <p>Essa é a forma interna</p>
</body>

### Formas externa
*Chamamos outro arquivo e informamos aonde está este arquivo*
<head>
    .....
    <title>Forma de utilizar o CSS</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <h2>Formas de utilizar o CSS</h2>
    <p>Ess é a forma externa.</p>    
</body>


## Principais Seletores de elemento
### Por Tipo (<" ">)
Seleciona todos os elementos do tipo <" "> inseridos
    Exemplo: 
    <p>
    <q>
    <x>
### Por Classe (.NomeClasse)
### Por Identificador (#paragrafo)
### Global (*)
### Descendente (main)
### Filhos (>)
### Principais Pseudo-Seletores
### Principais Pseudo-Elementos

## Unidades de medidas e cores

______________
## Referências:
- [CSS | MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [Seletores](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Selectors)
- [Jogo CSS diner](https://flukeout.github.io/)
- [Pseudo-Classes](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-classes)
- [Pseudo-Elementos](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-elements)