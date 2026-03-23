# core/estrategias.py
from core.estatisticas import detectar_rachas, detectar_alternancias
from core.estado import estado

PONTUACAO = {
    "racha_curta": 1,
    "racha_media": 2,
    "racha_longa": 3,
    "racha_extra_longa": 4,
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

    # Rachas
    rachas = detectar_rachas(historico, tamanho_min=2)
    for r in rachas:
        if r["tamanho"] == 2:
            resultados.append({"tipo":"racha_curta","detalhes":r,"pontos":PONTUACAO["racha_curta"]})
        elif r["tamanho"] == 3:
            resultados.append({"tipo":"racha_media","detalhes":r,"pontos":PONTUACAO["racha_media"]})
        elif r["tamanho"] == 4:
            resultados.append({"tipo":"racha_longa","detalhes":r,"pontos":PONTUACAO["racha_longa"]})
        elif r["tamanho"] >=5:
            resultados.append({"tipo":"racha_extra_longa","detalhes":r,"pontos":PONTUACAO["racha_extra_longa"]})

    # Alternâncias
    alternancias = detectar_alternancias(historico, tamanho_min=2)
    for alt in alternancias:
        if alt["tamanho"] == 2:
            resultados.append({"tipo":"alternancia_simples","detalhes":alt,"pontos":PONTUACAO["alternancia_simples"]})
        elif alt["tamanho"] == 4:
            resultados.append({"tipo":"alternancia_dupla","detalhes":alt,"pontos":PONTUACAO["alternancia_dupla"]})
        elif alt["tamanho"] >=6:
            resultados.append({"tipo":"alternancia_tripla","detalhes":alt,"pontos":PONTUACAO["alternancia_tripla"]})
        else:
            resultados.append({"tipo":"zig_zag","detalhes":alt,"pontos":PONTUACAO["zig_zag"]})

    # Tendências históricas
    total = len(historico)
    if total>0:
        cont_P = historico.count("P")
        cont_B = historico.count("B")

        if cont_P/total >=0.6:
            resultados.append({"tipo":"predominio","detalhes":{"lado":"P"},"pontos":PONTUACAO["predominio"]})
        elif cont_B/total >=0.6:
            resultados.append({"tipo":"predominio","detalhes":{"lado":"B"},"pontos":PONTUACAO["predominio"]})

        if len(rachas) >= total*0.3:
            resultados.append({"tipo":"sequencia_concentrada","detalhes":{"quantidade":len(rachas)},"pontos":PONTUACAO["sequencia_concentrada"]})

        if len(rachas)>0 and rachas[-1]["tamanho"]>=3 and historico[-1]!=rachas[-1]["tipo"]:
            resultados.append({"tipo":"tendencia_quebra","detalhes":{"inicio":rachas[-1]["inicio"],"quebra":historico[-1]},"pontos":PONTUACAO["tendencia_quebra"]})

    return resultados
