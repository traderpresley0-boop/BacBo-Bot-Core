let historicoUsuario = [
    "vermelho", "azul", "vermelho", "vermelho", "amarelo", "azul"
]; // O usuário pode atualizar manualmente o histórico

let historicoSinais = [];

// Estratégias do robô (modulares)
function estrategiaUltimaCor(rodadas) {
    if (rodadas.length === 0) return null;
    return rodadas[rodadas.length - 1]; // repete a última cor
}

function estrategiaSequencia(rodadas) {
    if (rodadas.length < 2) return null;
    const ultima = rodadas[rodadas.length - 1];
    const penultima = rodadas[rodadas.length - 2];
    return ultima === penultima ? ultima : null;
}

function estrategiaMaioria(rodadas) {
    if (rodadas.length === 0) return null;
    const contagem = { vermelho: 0, azul: 0, amarelo: 0 };
    rodadas.forEach(cor => contagem[cor]++);
    let maior = "vermelho";
    if (contagem.azul > contagem[maior]) maior = "azul";
    if (contagem.amarelo > contagem[maior]) maior = "amarelo";
    return maior;
}

function estrategiaAlternancia(rodadas) {
    if (rodadas.length < 2) return null;
    const ultima = rodadas[rodadas.length - 1];
    const penultima = rodadas[rodadas.length - 2];
    return ultima !== penultima ? ultima : null;
}

// Aplica todas as estratégias
function aplicarEstrategias(historico) {
    const sinais = [];
    const e1 = estrategiaUltimaCor(historico); if (e1) sinais.push(e1);
    const e2 = estrategiaSequencia(historico); if (e2) sinais.push(e2);
    const e3 = estrategiaMaioria(historico); if (e3) sinais.push(e3);
    const e4 = estrategiaAlternancia(historico); if (e4) sinais.push(e4);
    return sinais;
}

// Decisão final baseado na maioria das estratégias
function decidirFinal(sinais) {
    const contagem = { vermelho: 0, azul: 0, amarelo: 0 };
    sinais.forEach(cor => { if (cor) contagem[cor]++; });
    let decisao = "vermelho";
    if (contagem.azul > contagem[decisao]) decisao = "azul";
    if (contagem.amarelo > contagem[decisao]) decisao = "amarelo";
    return decisao;
}

// Atualiza o painel de histórico
function atualizarPainel() {
    const linhasContainer = document.getElementById("linhas");
    linhasContainer.innerHTML = "";

    historicoUsuario.forEach((resultado, index) => {
        const sinais = aplicarEstrategias(historicoUsuario.slice(0, index + 1));
        const decisao = decidirFinal(sinais);
        historicoSinais[index] = { sinais, decisao };

        const linha = document.createElement("div");
        linha.classList.add("linha");
        linha.innerHTML = `
            <div>${index + 1}</div>
            <div class="resultado ${resultado}">${resultado}</div>
            <div class="sinais">
                ${sinais.map(s => `<div class="sinal ${s}"></div>`).join("")}
            </div>
            <div class="decisao ${decisao}">${decisao}</div>
        `;
        linhasContainer.appendChild(linha);
    });
}

// Atualiza o status
function atualizarStatus() {
    const statusElem = document.getElementById("status");
    statusElem.innerHTML = `Status: <span class="ativo">Ativo</span>`;
}

// Inicializa painel e status
atualizarPainel();
atualizarStatus();
