let historico = [];
let intervalo;

// Atualiza status do robô
function atualizarStatus() {
    const status = "BacBo Bot ativo";
    document.getElementById('status').innerText = status;
}

// Gera rodada aleatória
function gerarRodada() {
    const numero = Math.floor(Math.random() * 10) + 1;
    const cor = Math.random() > 0.5 ? "vermelha" : "preta";
    return { numero, cor };
}

// Aplica 15 estratégias
function aplicarEstrategias(rodada) {
    let apostas = [];

    if (rodada.cor === "vermelha") apostas.push("apostar");
    if (rodada.cor === "preta") apostas.push("esperar");
    if (rodada.numero % 2 === 0) apostas.push("apostar");
    if (rodada.numero % 2 !== 0) apostas.push("esperar");
    if (rodada.numero > 5) apostas.push("apostar");
    if (rodada.numero <= 5) apostas.push("esperar");
    if (Math.random() > 0.5) apostas.push("apostar");

    if (historico.length > 0) {
        const ultima = historico[historico.length - 1].rodada;
        if (ultima.cor === rodada.cor) apostas.push("apostar");
        else apostas.push("esperar");
    }

    if (historico.length >= 2) {
        const penultima = historico[historico.length - 2].rodada.numero;
        const ultima = historico[historico.length - 1].rodada.numero;
        if ((ultima === penultima) && (rodada.numero === ultima)) apostas.push("apostar");
    }

    if (Math.random() > 0.7) apostas.push("apostar");
    if ([2,3,5,7].includes(rodada.numero)) apostas.push("apostar");
    if (![2,3,5,7].includes(rodada.numero)) apostas.push("esperar");
    if (historico.length > 0) {
        const ultimaCor = historico[historico.length - 1].rodada.cor;
        if (ultimaCor !== rodada.cor) apostas.push("apostar");
    }
    if (rodada.numero % 3 === 0) apostas.push("apostar");
    if (rodada.numero % 3 !== 0) apostas.push("esperar");

    return apostas;
}

// Decide ação final
function decidir(resultados) {
    const contar = { apostar: 0, esperar: 0 };
    resultados.forEach(r => {
        if (r === "apostar") contar.apostar++;
        else contar.esperar++;
    });
    return contar.apostar >= contar.esperar ? "apostar" : "esperar";
}

// Executa o robô
function rodarBot() {
    const rodada = gerarRodada();
    const resultados = aplicarEstrategias(rodada);
    const decisao = decidir(resultados);

    historico.push({ rodada, resultados, decisao });
    atualizarPainel();
    atualizarStatus();
}

// Atualiza painel
function atualizarPainel() {
    const painel = document.getElementById("painel");
    painel.innerHTML = historico.map((h, i) => {
        const classe = h.decisao === "apostar" ? "apostar" : "esperar";
        return `<div class="${classe}"><strong>Rodada ${i+1}</strong>: Número ${h.rodada.numero}, Cor ${h.rodada.cor} → <em>${h.decisao}</em></div>`;
    }).join("");
}

// Botões de controle
function iniciarBot() { intervalo = setInterval(rodarBot, 2000); }
function pararBot() { clearInterval(intervalo); }
function limparHistorico() { historico = []; atualizarPainel(); }

// Inicializa status e painel
atualizarStatus();
atualizarPainel();
