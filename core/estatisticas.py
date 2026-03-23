# core/estatisticas.py
from collections import Counter

def calcular_frequencia(historico):
    total = len(historico)
    contagem = Counter(historico)
    frequencia = {
        "contagem": {"P": contagem.get("P", 0), "B": contagem.get("B", 0)},
        "percentual": {
            "P": round(contagem.get("P",0)/total*100,2) if total else 0,
            "B": round(contagem.get("B",0)/total*100,2) if total else 0
        }
    }
    return frequencia

def detectar_rachas(historico, tamanho_min=2):
    rachas = []
    if not historico:
        return rachas

    atual = historico[0]
    tamanho = 1
    inicio = 0

    for i in range(1,len(historico)):
        if historico[i] == atual:
            tamanho += 1
        else:
            if tamanho >= tamanho_min:
                rachas.append({"tipo": atual, "tamanho": tamanho, "inicio": inicio})
            atual = historico[i]
            tamanho = 1
            inicio = i
    if tamanho >= tamanho_min:
        rachas.append({"tipo": atual, "tamanho": tamanho, "inicio": inicio})

    return rachas

def detectar_alternancias(historico, tamanho_min=2):
    alternancias = []
    if len(historico) < tamanho_min:
        return alternancias

    seq = [historico[0]]
    inicio = 0

    for i in range(1,len(historico)):
        if historico[i] != historico[i-1]:
            seq.append(historico[i])
        else:
            if len(seq) >= tamanho_min:
                alternancias.append({"padrao": seq.copy(), "inicio": inicio, "tamanho": len(seq)})
            seq = [historico[i]]
            inicio = i
    if len(seq) >= tamanho_min:
        alternancias.append({"padrao": seq.copy(), "inicio": inicio, "tamanho": len(seq)})

    return alternancias
