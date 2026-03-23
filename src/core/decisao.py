def decidir(resultados):
    # Exemplo: aposta se pelo menos metade das estratégias recomendam
    acoes = [r["acao"] for r in resultados]
    if acoes.count("apostar") >= len(acoes)/2:
        return "apostar"
    return "esperar"
