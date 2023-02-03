// Variáveis = Um espaço da memória do servidor que guardamos algo, um numero, letra, texto, imagem..
//FUNÇÃO = Um trecho de código que só é executado quando chamado


//let nome = "Aldruin"; // let cria a variavel Nome com o valor Aldruin.


//console.log(nome); // console é a função que executa o nome

//function Umdois(){
    //console.log(nome);
  //  console.log("Estou dentro da função");
//}

//Umdois(); // Umdois é executado quando chamado (Chamando a função)

let chave = "e0122df7d2c084aeaacfd6c3a7d59272"

function colocarNaTela(dados){
    //console.log(dados)
    document.querySelector(".cidade").innerHTML = "Tempo em " + dados.name
    document.querySelector(".temperatura").innerHTML = Math.floor(dados.main.temp) + "°C"
    document.querySelector(".descricao").innerHTML = dados.weather[0].description
    document.querySelector(".umidade").innerHTML = "Umidade em " + dados.main.humidity + "%"
    document.querySelector(".icone") .src = "https://openweathermap.org/img/wn/" + dados.weather[0].icon + ".png"
}

async function buscarCidade(cidade){
    let dados = await fetch("https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=" + chave + "&lang=pt_br" + "&units=metric")
    .then( resposta => resposta.json())
     colocarNaTela(dados)
}
function cliqueinobotao(){
    let cidade = document.querySelector(".pesquisa").value
    
    buscarCidade(cidade)
}

