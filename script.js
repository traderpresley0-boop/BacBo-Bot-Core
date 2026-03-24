let historico = JSON.parse(localStorage.getItem("historico")) || [];
let banca = parseInt(localStorage.getItem("banca")) || 5000;

function login() {
  let senha = document.getElementById("senha").value;

  let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$/;

  if (!regex.test(senha)) {
    alert("Senha fraca!");
    return;
  }

  document.getElementById("login").style.display = "none";
  document.getElementById("app").classList.remove("hidden");

  atualizar();
  atualizarBanca();
}

function add(cor) {
  historico.push(cor);
  localStorage.setItem("historico", JSON.stringify(historico));
  atualizar();
}

function atualizar() {
  let lista = document.getElementById("lista");
  lista.innerHTML = "";

  historico.slice(-15).forEach(c => {
    let span = document.createElement("span");

    if (c === "azul") span.innerHTML = "🔵";
    if (c === "vermelho") span.innerHTML = "🔴";
    if (c === "amarelo") span.innerHTML = "🟡";

    lista.appendChild(span);
  });
}

/* MULTI ESTRATÉGIAS */
function analisar() {
  document.getElementById("resultado").innerHTML = "";
  document.getElementById("loading").classList.remove("hidden");

  setTimeout(() => {

    let ultimos = historico.slice(-5);

    let estrategia1 = tendencia(ultimos);
    let estrategia2 = reversao(ultimos);
    let estrategia3 = alternancia(ultimos);

    let final = escolherMelhor([estrategia1, estrategia2, estrategia3]);

    document.getElementById("loading").classList.add("hidden");
    document.getElementById("resultado").innerHTML =
      "🎯 " + final + "<br>🟡 Proteção: EMPATE";

  }, 2500);
}

/* ESTRATÉGIAS */

function tendencia(arr) {
  let azul = arr.filter(x => x === "azul").length;
  let vermelho = arr.filter(x => x === "vermelho").length;
  return azul > vermelho ? "🔵 BIG" : "🔴 SMALL";
}

function reversao(arr) {
  let ultimo = arr[arr.length - 1];
  return ultimo === "azul" ? "🔴 SMALL" : "🔵 BIG";
}

function alternancia(arr) {
  let ultimo = arr[arr.length - 1];
  let penultimo = arr[arr.length - 2];

  if (ultimo !== penultimo) return ultimo === "azul" ? "🔴 SMALL" : "🔵 BIG";
  return "🔵 BIG";
}

/* ESCOLHER MELHOR */
function escolherMelhor(lista) {
  let random = Math.floor(Math.random() * lista.length);
  return lista[random];
}

/* BANCA */

function win() {
  banca += 1000;
  salvarBanca();
}

function loss() {
  banca -= 1000;
  salvarBanca();

  if (banca <= 2000) {
    alert("⚠️ STOP LOSS ATINGIDO!");
  }
}

function salvarBanca() {
  localStorage.setItem("banca", banca);
  atualizarBanca();
}

function atualizarBanca() {
  document.getElementById("banca").innerText = banca;
}
