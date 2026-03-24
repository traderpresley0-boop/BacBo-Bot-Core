let historico = [];
let banca = 5000;

function login() {
  let senha = document.getElementById("senha").value;

  if (senha.length < 6) {
    alert("Senha fraca!");
    return;
  }

  document.getElementById("login").style.display = "none";
  document.getElementById("app").classList.remove("hidden");
}

function add(cor) {
  historico.push(cor);
  atualizar();
}

function atualizar() {
  let lista = document.getElementById("lista");
  lista.innerHTML = "";

  historico.slice(-10).forEach(c => {
    let span = document.createElement("span");

    if (c === "azul") span.innerHTML = "🔵";
    if (c === "vermelho") span.innerHTML = "🔴";
    if (c === "amarelo") span.innerHTML = "🟡";

    lista.appendChild(span);
  });
}

function analisar() {
  let res = document.getElementById("resultado");
  let load = document.getElementById("loading");

  res.innerHTML = "";
  load.classList.remove("hidden");

  setTimeout(() => {

    let ult = historico.slice(-3);
    let azul = ult.filter(x => x === "azul").length;
    let vermelho = ult.filter(x => x === "vermelho").length;

    let sinal = azul > vermelho ? "🔴 SMALL" : "🔵 BIG";

    load.classList.add("hidden");
    res.innerHTML = "> " + sinal + "<br>> 🟡 PROTEÇÃO";

  }, 2000);
}

function win() {
  banca += 1000;
  atualizarBanca();
}

function loss() {
  banca -= 1000;
  atualizarBanca();

  if (banca <= 2000) {
    alert("STOP LOSS ATINGIDO!");
  }
}

function atualizarBanca() {
  document.getElementById("banca").innerText = banca;
}
