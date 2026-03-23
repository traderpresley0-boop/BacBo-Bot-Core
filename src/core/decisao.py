def decidir(resultados):
    """
    Decide a ação final do robô com base nos resultados das estratégias.
    Se pelo menos metade das estratégias recomendam apostar, retorna 'apostar'.
    """
    acoes = [r["acao"] for r in resultados]
    if acoes.count("apostar") >= len(acoes)/2:
        return "apostar"
    return "esperar"
