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
[CSS | MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/CSS)

[Seletores](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Selectors)

[Jogo CSS diner](https://flukeout.github.io/)

[Pseudo-Classes](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-classes)

[Pseudo-Elementos](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-elements)

[ARTIGO Propriedade border no CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/border?retiredLocale=pt-PT)

[ARTIGO Propriedade border-radius no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/border-radius)

[ARTIGO Propriedade box-shadow no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/box-shadow)

[ARTIGO Propriedade cursor no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/cursor)

[ARTIGO Propriedade outline no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/outline)

[ARTIGO Propriedade float no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/float)

[ARTIGO Propriedade overflow no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/overflow)

[ARTIGO Propriedade font-size no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-size)

[ARTIGO Propriedade font-weight no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-weight)

[ARTIGO Propriedade text-align no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-align)

[ARTIGO Propriedade text-indent no CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent)

[ARTIGO Propriedade letter-spacing no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/letter-spacing)

[ARTIGO Propriedade line-height no CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)

[ARTIGO Propriedade list-style no CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style?retiredLocale=pt-PT)

[ARTIGO Propriedade text-decoration no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-decoration)

[ARTIGO Propriedade background no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background)

[ARTIGO Referências de CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Reference)

[ARTIGO Como usar herança no CSS?](https://tableless.com.br/afinal-como-usar-heranca-no-css/)

[ARTIGO Trabalhando com transições no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

[ARTIGO Trabalhando com animações no CSS](https://codepen.io/afonsopacifer/post/hora-de-aventura-com-css-5-animacoes)

[ARTIGO Função scale no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transform-function/scale)

[ARTIGO Função rotate no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transform-function/rotate)

[ARTIGO Função translate no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transform-function/translate)

[ARTIGO Função skew no CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/skew)

[ARTIGO Trabalhando com transformações no CSS](https://codepen.io/afonsopacifer/post/hora-de-aventura-com-css-3-transformacoes)

[ARTIGO Propriedade opacity no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/opacity)

[ARTIGO Box model para iniciantes](https://tableless.github.io/iniciantes/manual/css/box-model.html)

[ARTIGO Trabalhando com Flexbox](https://codepen.io/afonsopacifer/post/hora-de-aventura-com-css-9-flexbox)

[ARTIGO Conceitos básicos do Flexbox](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)

[ARTIGO Guia completo Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

[JOGO Flexbox Froggy](https://flexboxfroggy.com/)

[ARTIGO Conceitos básicos de Grid Layout](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout)

[ARTIGO Entendendo o CSS Grid Layout](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Grid_Layout)

[ARTIGO Guia completo Grid Layout](https://css-tricks.com/snippets/css/complete-guide-grid/)

[JOGO CSS Grid Garden](https://cssgridgarden.com/)

[ARTIGO CSS Grid e Flexbox - Quando utilizar?](https://felipefialho.com/blog/css-grid-e-flexbox-quando-utilizar/)

[ARTIGO Usando Media Queries no CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_media_queries/Using_media_queries)

[ARTIGO Trabalhando com viewport no CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)

[ARTIGO Trabalhando com imagens responsivas no CSS](https://developer.mozilla.org/pt-BR/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

[ARTIGO Entendendo o BEM no CSS](https://desenvolvimentoparaweb.com/css/bem/)

[ARTIGO Organize seu CSS com SMACSS, BEM e SASS](https://medium.com/@larymagal/organize-seu-css-com-smacss-bem-e-sass-7e8f50a41544)

[ARTIGO Entendendo Arquiteturas CSS](https://medium.com/tableless/arquitetura-css-d344fb01dd18)

[ARTIGO Semantic UI](https://semantic-ui.com/)

[ARTIGO Tailwind CSS](https://tailwindcss.com/)

[ARTIGO Foundation](https://get.foundation/)

[ARTIGO Bootstrap](https://getbootstrap.com.br/)

[ARTIGO SASS](https://sass-lang.com/)

[ARTIGO Stylus](https://stylus-lang.com/)

[ARTIGO CSS Lint](http://csslint.net/)

[ARTIGO Normalize CSS](https://necolas.github.io/normalize.css/)

[ARTIGO Reset CSS](https://meyerweb.com/eric/tools/css/reset/)

[ARTIGO Styled-components](https://styled-components.com/)

[ARTIGO Do Sass e BEM ao CSS-in-JS: A (re)evolução do CSS ao longo da história](https://felipefialho.com/blog/do-sass-e-bem-ao-css-in-js-a-evolucao-do-css-ao-longo-da-historia/)

__________________
[ARTIGO Iconmonstr](https://iconmonstr.com/)

[ARTIGO Por que usar SVG?](https://willianjusten.com.br/por-que-usar-svg)

[ARTIGO Entenda o SVG](https://developer.mozilla.org/pt-BR/docs/Glossary/SVG)

[ARTIGO Utilizando variáreis CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Using_CSS_custom_properties)

[ARTIGO Criando e hospedando seu site de graça no GitHub Pages](https://woliveiras.com.br/posts/jamstack-criando-e-hospedando-seu-site-de-gra%C3%A7a-no-github-pages/)

[ARTIGO Aprendendo sobre o GitHub Pages](https://docs.github.com/pt/pages/getting-started-with-github-pages/about-github-pages)