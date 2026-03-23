# core/estrategias.py
from core.estatisticas import detectar_rachas, detectar_alternancias
from core.estado import estado

# Pontuação inicial para cada estratégia
PONTUACAO = {
    "racha_curta": 1,
    "racha_media": 2,
    "racha_longa": 3,
    "racha_extra_longa": 4,
    "racha_invertida": 2,
    "alternancia_simples": 1,
    "alternancia_dupla": 2,
    "alternancia_tripla": 3,
    "zig_zag": 2,
    "racha_alternancia": 2,
    "alternancia_racha": 2,
    "predominio": 2,
    "sequencia_concentrada": 2,
    "tendencia_quebra": 3
}

def analisar_estrategias(historico):
    resultados = []

    # 1. Rachas
    rachas = detectar_rachas(historico, tamanho_min=2)
    for r in rachas:
        if r["tamanho"] == 2:
            resultados.append({"tipo": "racha_curta", "detalhes": r, "pontos": PONTUACAO["racha_curta"]})
        elif r["tamanho"] == 3:
            resultados.append({"tipo": "racha_media", "detalhes": r, "pontos": PONTUACAO["racha_media"]})
        elif r["tamanho"] == 4:
            resultados.append({"tipo": "racha_longa", "detalhes": r, "pontos": PONTUACAO["racha_longa"]})
        elif r["tamanho"] >= 5:
            resultados.append({"tipo": "racha_extra_longa", "detalhes": r, "pontos": PONTUACAO["racha_extra_longa"]})

    # 2. Alternâncias
    alternancias = detectar_alternancias(historico, tamanho_min=2)
    for alt in alternancias:
        if alt["tamanho"] == 2:
            resultados.append({"tipo": "alternancia_simples", "detalhes": alt, "pontos": PONTUACAO["alternancia_simples"]})
        elif alt["tamanho"] == 4:
            resultados.append({"tipo": "alternancia_dupla", "detalhes": alt, "pontos": PONTUACAO["alternancia_dupla"]})
        elif alt["tamanho"] >= 6:
            resultados.append({"tipo": "alternancia_tripla", "detalhes": alt, "pontos": PONTUACAO["alternancia_tripla"]})
        else:
            resultados.append({"tipo": "zig_zag", "detalhes": alt, "pontos": PONTUACAO["zig_zag"]})

    # 3. Combinações Racha + Alternância
    # Exemplo simplificado: racha seguida de alternância
    for i in range(len(historico)-2):
        bloco = historico[i:i+4]
        if len(bloco) == 4 and bloco[0] == bloco[1] and bloco[2] != bloco[3]:
            resultados.append({"tipo": "racha_alternancia", "detalhes": {"inicio": i, "bloco": bloco}, "pontos": PONTUACAO["racha_alternancia"]})
        elif len(bloco) == 4 and bloco[0] != bloco[1] and bloco[2] == bloco[3]:
            resultados.append({"tipo": "alternancia_racha", "detalhes": {"inicio": i, "bloco": bloco}, "pontos": PONTUACAO["alternancia_racha"]})

    # 4. Tendências Históricas
    total = len(historico)
    if total > 0:
        contagem_P = historico.count("P")
        contagem_B = historico.count("B")

        if contagem_P / total >= 0.6:
            resultados.append({"tipo": "predominio", "detalhes": {"lado": "P"}, "pontos": PONTUACAO["predominio"]})
        elif contagem_B / total >= 0.6:
            resultados.append({"tipo": "predominio", "detalhes": {"lado": "B"}, "pontos": PONTUACAO["predominio"]})

        # Sequência concentrada: rachas curtas frequentes
        if len(rachas) >= total * 0.3:
            resultados.append({"tipo": "sequencia_concentrada", "detalhes": {"quantidade": len(rachas)}, "pontos": PONTUACAO["sequencia_concentrada"]})

        # Tendência de quebra: último resultado quebra racha longa
        if len(rachas) > 0 and rachas[-1]["tamanho"] >= 3 and historico[-1] != rachas[-1]["tipo"]:
            resultados.append({"tipo": "tendencia_quebra", "detalhes": {"inicio": rachas[-1]["inicio"], "quebra": historico[-1]}, "pontos": PONTUACAO["tendencia_quebra"]})

    return resultados

# Função de teste rápido
def mostrar_analise():
    historico = estado["historico"]
    analise = analisar_estrategias(historico)
    for item in analise:
        print(item)
