# core/estado.py

estado = {
    "historico": [],             # lista de resultados
    "total_jogadas": 0,          # contador total
    "contagem": {"P": 0, "B": 0}, # contagem de Player e Banker
    "sequencia_atual": {"tipo": None, "tamanho": 0} # sequência em andamento
}

def atualizar_estado(resultado):
    valor = resultado["valor"]

    # Atualiza histórico
    estado["historico"].append(valor)
    estado["total_jogadas"] += 1
    estado["contagem"][valor] += 1

    # Atualiza sequência
    if estado["sequencia_atual"]["tipo"] == valor:
        estado["sequencia_atual"]["tamanho"] += 1
    else:
        estado["sequencia_atual"]["tipo"] = valor
        estado["sequencia_atual"]["tamanho"] = 1
