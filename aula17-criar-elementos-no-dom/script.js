const arrayPostagens = [
  {
    titulo: "Pop Vegan",
    subtitulo: "Comida vegana para todos!",
    data: "06/07/2022",
    texto: "Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)"
  },
  {
    titulo: "Make Hommus. Not War",
    subtitulo: "Só delivery, para curtir em casa!",
    data: "18/08/2022",
    texto: "Neste restaurante não só pode, como é encorajado comer o antepasto como prato principal. Recomendamos os kibes e a kafta bonina."
  },
  {
    titulo: "Churrascada do Mar",
    subtitulo: "Melhor do que estar na praia!",
    data: "30/08/2022",
    texto: "Todos conhecemos e amamos um bom churrasco, mas o que você acha de experimentar um churrasco focado em frutos do mar? Nós gostamos, experimente e nos conte o que você achou!"
  },
]

// // console.table(arrayPostagens)

// // // crie um elemento HMTL
// // const article1 = document.createElement("article1")
// // const article2 = document.createElement("article2")

// // inserindo conteúdo
// article1.innerHTML = `
//   <h3>Pop Vegan</h3>
//   <p class="subtitulo">Comida vegana para todos!</p>
//   <div class="data">06/07/2022</div>
//   <p>Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)</p>`

//   article2.innerHTML = `
//   <h3>${arrayPostagens[1].titulo}</h3>
//   <p class="subtitulo">${arrayPostagens[1].subtitulo}</p>
//   <div class="data">${arrayPostagens[1].data}</div>
//   <p>${arrayPostagens[1].texto}</p>`

// // recorte para esse elemento o conteúdo HTML do #post-1
// const main = document.querySelector("main")

// // adicione o elemento à tag main
// main.appendChild(article)
// main.appendChild(article2)

// loop para geração dos elementos de forma incremental
for (let i = 0; i < arrayPostagens.length; i++){
  
  // crie um elemento HMTL
  const article = document.createElement("article")

  // inserindo conteúdo
  article.innerHTML = `
    <h3>${arrayPostagens[i].titulo}</h3>
    <p class="subtitulo">${arrayPostagens[i].subtitulo}</p>
    <div class="data">${arrayPostagens[i].data}</div>
    <p>${arrayPostagens[i].texto}</p>
    `
  
  // adicione o elemento à tag main
  main.appendChild(article)
}