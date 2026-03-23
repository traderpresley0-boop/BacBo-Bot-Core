let historicoUsuario = ["vermelho","azul","vermelho","vermelho","amarelo","azul"];
let historicoSinais = [];

// Função para gerar centenas de estratégias automaticamente
function gerarSinais(historico){
    const sinais = [];
    const cores = ["vermelho","azul","amarelo"];

    // Gera estratégias com janelas de 1 a 50 rodadas
    for(let N=1; N<=50; N++){
        const ultimas = historico.slice(-N);

        if(!ultimas.length) continue;

        // Última cor
        sinais.push(ultimas[ultimas.length-1]);

        // Maioria recente
        const contagem = {vermelho:0, azul:0, amarelo:0};
        ultimas.forEach(c => contagem[c]++);
        let maior = "vermelho";
        if(contagem.azul>contagem[maior]) maior="azul";
        if(contagem.amarelo>contagem[maior]) maior="amarelo";
        sinais.push(maior);

        // Alternância
        if(ultimas.length>=2){
            const alt = ultimas[ultimas.length-1] !== ultimas[ultimas.length-2] ? ultimas[ultimas.length-1] : null;
            if(alt) sinais.push(alt);
        }

        // Frequência de Tie
        const contTie = ultimas.filter(c => c==="amarelo").length;
        if(contTie >= 2) sinais.push("amarelo");
    }

    return sinais;
}

// Decisão final baseada na maioria dos sinais
function decidirFinal(sinais){
    const contagem = {vermelho:0, azul:0, amarelo:0};
    sinais.forEach(c => { if(c) contagem[c]++ });
    let decisao="vermelho";
    if(contagem.azul>contagem[decisao]) decisao="azul";
    if(contagem.amarelo>contagem[decisao]) decisao="amarelo";
    return decisao;
}

// Atualiza painel
function atualizarPainel(){
    const container = document.getElementById("linhas");
    container.innerHTML = "";

    historicoUsuario.forEach((res,index)=>{
        const sinais = gerarSinais(historicoUsuario.slice(0,index+1));
        const decisao = decidirFinal(sinais);
        historicoSinais[index] = {sinais,decisao};

        const linha = document.createElement("div");
        linha.classList.add("linha");
        linha.innerHTML = `
            <div>${index+1}</div>
            <div class="resultado ${res}">${res}</div>
            <div class="sinais">${sinais.map(s=>`<div class="sinal ${s}"></div>`).join("")}</div>
            <div class="decisao ${decisao}">${decisao}</div>
        `;
        container.appendChild(linha);
    });
}

// Atualiza status
function atualizarStatus(){
    const statusElem = document.getElementById("status");
    statusElem.innerHTML=`Status: <span class="ativo">Ativo</span>`;
}

// Adicionar rodada manual
document.getElementById("adicionarRodada").addEventListener("click",()=>{
    const cor = document.getElementById("novaCor").value;
    historicoUsuario.push(cor);
    atualizarPainel();
    atualizarStatus();
});

// Inicializa
atualizarPainel();
atualizarStatus();
