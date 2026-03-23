// ==================================================
// BacBo Bot - Lógica 100% JavaScript para GitHub Pages
// Atualiza painel e histórico automaticamente
// ==================================================

// Histórico de rodadas
let historico = [];

// Simula o status do robô
function atualizarStatus() {
    const status = "BacBo Bot ativo";
    document.getElementById('status').innerText = status;
}

// ==================================================
// Função: gerarRodada
// Gera número (1-10) e cor aleatória (vermelha ou preta)
// ==================================================
function gerarRodada() {
    const numero = Math.floor(Math.random() * 10) + 1;
    const cor = Math.random() > 0.5 ? "vermelha" : "preta";
    return { numero, cor };
}

// ==================================================
// Função: aplicarEstrategias
// Aplica 15 estratégias simuladas
// ==================================================
function aplicarEstrategias(rodada) {
    let apostas = [];

    // Estratégia 1: Cor vermelha
    if (rodada.cor === "vermelha") apostas.push("apostar");

    // Estratégia 2: Cor preta
    if (rodada.cor === "preta") apostas.push("esperar");

    // Estratégia 3: Número par
    if (rodada.numero % 2 === 0) apostas.push("apostar");

    // Estratégia 4: Número ímpar
    if (rodada.numero % 2 !== 0) apostas.push("esperar");

    // Estratégia 5: Número maior que 5
    if (rodada.numero > 5) apostas.push("apostar");

    // Estratégia 6: Número menor ou igual a 5
    if (rodada.numero <= 5) apostas.push("esperar");

    // Estratégia 7: Aleatória ponderada
    if (Math.random() > 0.5) apostas.push("apostar");

    // Estratégia 8: Tendência simulada
    if (historico.length > 0) {
        const ultima = historico[historico.length - 1].rodada;
        if (ultima.cor === rodada.cor) apostas.push("apostar");
        else apostas.push("esperar");
    }

    // Estratégia 9: Racha de números consecutivos
    if (historico.length >= 2) {
        const penultima = historico[historico.length - 2].rodada.numero;
        const ultima = historico[historico.length - 1].rodada.numero;
        if ((ultima === penultima) && (rodada.numero === ultima)) apostas.push("apostar");
    }

    // Estratégia 10: Simulação de padrão aleatório
    if (Math.random() > 0.7) apostas.push("apostar");

    // Estratégia 11: Número prime (2,3,5,7)
    if ([2,3,5,7].includes(rodada.numero)) apostas.push("apostar");

    // Estratégia 12: Número não prime
    if (![2,3,5,7].includes(rodada.numero)) apostas.push("esperar");

    // Estratégia 13: Alternância de cores
    if (historico.length > 0) {
        const ultimaCor = historico[historico.length - 1].rodada.cor;
        if (ultimaCor !== rodada.cor) apostas.push("apostar");
    }

    // Estratégia 14: Número múltiplo de 3
    if (rodada.numero % 3 === 0) apostas.push("apostar");

    // Estratégia 15: Número não múltiplo de 3
    if (rodada.numero % 3 !== 0) apostas.push("esperar");

    return apostas;
}

// ==================================================
// Função: decidir
// Decide ação final: apostar se maioria das estratégias sugerirem apostar
// ==================================================
function decidir(resultados) {
    const contar = { apostar: 0, esperar: 0 };
    resultados.forEach(r => {
        if (r === "apostar") contar.apostar++;
        else contar.esperar++;
    });
    return contar.apostar >= contar.esperar ? "apostar" : "esperar";
}

// ==================================================
// Função: rodarBot
// Gera rodada, aplica estratégias, decide e atualiza histórico
// ==================================================
function rodarBot() {
    const rodada = gerarRodada();
    const resultados = aplicarEstrategias(rodada);
    const decisao = decidir(resultados);

    historico.push({ rodada, resultados, decisao });
    atualizarPainel();
    atualizarStatus();
}

// ==================================================
// Função: atualizarPainel
// Mostra histórico das rodadas no HTML
// ==================================================
function atualizarPainel() {
    const painel = document.getElementById("painel");
    painel.innerHTML = historico.map((h, i) => {
        return `<div>
            <strong>Rodada ${i+1}</strong>: Número ${h.rodada.numero}, Cor ${h.rodada.cor} → <em>${h.decisao}</em>
        </div>`;
    }).join("");
}

// ==================================================
// Executa o robô a cada 2 segundos
// ==================================================
setInterval(rodarBot, 2000);

// Atualiza status na primeira carga
atualizarStatus();
