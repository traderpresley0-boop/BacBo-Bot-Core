const API_URL = "https://meu-bacbo-api.onrender.com";

const entradaInput = document.getElementById("entrada");
const enviarBtn = document.getElementById("enviar");
const resetarBtn = document.getElementById("resetar");

const historicoDiv = document.getElementById("historico");
const sequenciaSpan = document.getElementById("sequencia");
const contagemSpan = document.getElementById("contagem");
const pontosSpan = document.getElementById("pontos");
const padraoSpan = document.getElementById("padrao");
const riscoSpan = document.getElementById("risco");

// Atualiza o estado do bot na interface
async function atualizarEstado() {
    try {
        const res = await fetch(`${API_URL}/estado`);
        const data = await res.json();

        // Histórico
        historicoDiv.innerHTML = "";
        data.historico.forEach(item => {
            const bola = document.createElement("div");
            bola.classList.add("bolinha", item);
            historicoDiv.appendChild(bola);
        });

        // Sequência atual
        sequenciaSpan.textContent = `${data.sequencia.tipo || "-"} x ${data.sequencia.tamanho || 0}`;

        // Contagem
        contagemSpan.textContent = `P: ${data.contagem.P || 0} / B: ${data.contagem.B || 0}`;

        // Pontuação e padrão forte ficam vazios até enviar nova entrada
        pontosSpan.textContent = "-";
        padraoSpan.textContent = "-";

        // Risco com cores de alerta
        riscoSpan.textContent = `Banca: ${data.risco.banca} | Lucro: ${data.risco.lucro} | Perda: ${data.risco.perda}`;
        riscoSpan.classList.remove("limite-alto", "limite-crítico");
        if (!data.risco.limites_ok) {
            riscoSpan.classList.add("limite-crítico");
        } else if (data.risco.perda >= (data.risco.banca * 0.5)) { // exemplo de alerta intermediário
            riscoSpan.classList.add("limite-alto");
        }
    } catch (err) {
        console.error("Erro ao atualizar estado:", err);
    }
}

// Envia resultado P/B para a API
enviarBtn.addEventListener("click", async () => {
    const valor = entradaInput.value.toUpperCase();
    if (valor !== "P" && valor !== "B") return alert("Use apenas P ou B");

    try {
        const res = await fetch(`${API_URL}/entrada`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ resultado: valor })
        });
        const data = await res.json();

        // Atualiza histórico
        historicoDiv.innerHTML = "";
        data.historico.forEach(item => {
            const bola = document.createElement("div");
            bola.classList.add("bolinha", item);
            historicoDiv.appendChild(bola);
        });

        // Atualiza outras informações
        sequenciaSpan.textContent = `${data.sequencia.tipo || "-"} x ${data.sequencia.tamanho || 0}`;
        contagemSpan.textContent = `P: ${data.contagem.P || 0} / B: ${data.contagem.B || 0}`;
        pontosSpan.textContent = data.pontos;
        padraoSpan.textContent = data.padrao_forte;
        riscoSpan.textContent = `Banca: ${data.risco.banca} | Lucro: ${data.risco.lucro} | Perda: ${data.risco.perda}`;
        riscoSpan.classList.remove("limite-alto", "limite-crítico");
        if (!data.risco.limites_ok) {
            riscoSpan.classList.add("limite-crítico");
        } else if (data.risco.perda >= (data.risco.banca * 0.5)) {
            riscoSpan.classList.add("limite-alto");
        }
    } catch (err) {
        console.error("Erro ao enviar entrada:", err);
    }
});

// Reseta o bot
resetarBtn.addEventListener("click", async () => {
    await fetch(`${API_URL}/reset`, { method: "POST" });
    atualizarEstado();
});

// Atualiza estado automaticamente a cada 2 segundos
setInterval(atualizarEstado, 2000);
atualizarEstado();
