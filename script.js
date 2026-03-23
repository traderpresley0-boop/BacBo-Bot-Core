let historicoUsuario = JSON.parse(localStorage.getItem("historico")) || [];
let historicoSinais = [];

// Estratégias ponderadas e escaláveis
function gerarSinais(historico){
    const sinais = [];
    const cores = ["vermelho","azul","amarelo"];

    for(let N=1; N<=50; N++){
        const ultimas = historico.slice(-N);
        if(!ultimas.length) continue;

        // Última cor
        sinais.push({cor: ultimas[ultimas.length-1], peso: 1 + N/50});

        // Maioria recente
        const contagem = {vermelho:0, azul:0, amarelo:0};
        ultimas.forEach(c => contagem[c]++);
        let maior = "vermelho";
        if(contagem.azul>contagem[maior]) maior="azul";
        if(contagem.amarelo>contagem[maior]) maior="amarelo";
        sinais.push({cor: maior, peso: 1 + N/50});

        // Alternância
        if(ultimas.length>=2){
            const alt = ultimas[ultimas.length-1] !== ultimas[ultimas.length-2] ? ultimas[ultimas.length-1] : null;
            if(alt) sinais.push({cor: alt, peso: 0.5});
        }

        // Frequência Tie
        const contTie = ultimas.filter(c => c==="amarelo").length;
        if(contTie>=2) sinais.push({cor:"amarelo", peso:1});
    }

    return sinais;
}

// Decisão final ponderada
function decidirFinal(sinais){
    const contagem = {vermelho:0, azul:0, amarelo:0};
    sinais.forEach(s => { if(s) contagem[s.cor] += s.peso; });
    let decisao="vermelho";
    if(contagem.azul>contagem[decisao]) decisao="azul";
    if(contagem.amarelo>contagem[decisao]) decisao="amarelo";
    return decisao;
}

// Atualiza barras de frequência
function atualizarBarras(){
    const contagem = {vermelho:0, azul:0, amarelo:0};
    historicoUsuario.forEach(c => contagem[c]++);
    const total = historicoUsuario.length || 1;

    document.getElementById("cont-vermelho").innerText = contagem.vermelho;
    document.getElementById("cont-azul").innerText = contagem.azul;
    document.getElementById("cont-amarelo").innerText = contagem.amarelo;

    document.getElementById("bar-vermelho").style.width = (contagem.vermelho/total*100) + "%";
    document.getElementById("bar-azul").style.width = (contagem.azul/total*100) + "%";
    document.getElementById("bar-amarelo").style.width = (contagem.amarelo/total*100) + "%";
}

// Atualiza painel e gráfico
function atualizarPainel(){
    const container = document.getElementById("linhas");
    container.innerHTML = "";

    let datasetDecisao = [];

    historicoUsuario.forEach((res,index)=>{
        const sinais = gerarSinais(historicoUsuario.slice(0,index+1));
        const decisao = decidirFinal(sinais);
        historicoSinais[index] = {sinais,decisao};
        datasetDecisao.push(decisao);

        const linha = document.createElement("div");
        linha.classList.add("linha");
        linha.innerHTML = `
            <div>${index+1}</div>
            <div class="resultado ${res}">${res}</div>
            <div class="sinais">${sinais.map(s=>`<div class="sinal ${s.cor}"></div>`).join("")}</div>
            <div class="decisao ${decisao}">${decisao}</div>
        `;
        container.appendChild(linha);
    });

    atualizarBarras();
    atualizarGrafico(datasetDecisao);
}

// Atualiza status
function atualizarStatus(){
    const statusElem = document.getElementById("status");
    statusElem.innerHTML=`Status: <span class="ativo">Ativo</span>`;
}

// Adicionar rodada
document.getElementById("adicionarRodada").addEventListener("click",()=>{
    const cor = document.getElementById("novaCor").value;
    historicoUsuario.push(cor);
    localStorage.setItem("historico", JSON.stringify(historicoUsuario));
    atualizarPainel();
    atualizarStatus();
});

// Reset histórico
document.getElementById("resetHistorico").addEventListener("click",()=>{
    historicoUsuario = [];
    localStorage.removeItem("historico");
    atualizarPainel();
    atualizarStatus();
});

// Exportar histórico
document.getElementById("exportHistorico").addEventListener("click",()=>{
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(historicoUsuario));
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute("href", dataStr);
    dlAnchor.setAttribute("download","historico_bacbo.json");
    dlAnchor.click();
});

// Gráfico com Chart.js
let chart=null;
function atualizarGrafico(decisoes){
    const ctx = document.getElementById('tendenciaChart').getContext('2d');
    const labels = decisoes.map((_,i)=>i+1);

    if(chart) chart.destroy();
    chart = new Chart(ctx,{
        type:'line',
        data:{
            labels: labels,
            datasets:[{
                label:'Decisão Final',
                data:decisoes.map(d=>d==="vermelho"?1:d==="azul"?2:3),
                fill:false,
                borderColor:'#ffd700',
                tension:0.3
            }]
        },
        options:{
            scales:{
                y:{
                    ticks:{
                        callback:function(val){ return val===1?"Vermelho":val===2?"Azul":"Amarelo"; }
                    },
                    min:0.8, max:3.2
                }
            }
        }
    });
}

// Inicializa
atualizarPainel();
atualizarStatus();
