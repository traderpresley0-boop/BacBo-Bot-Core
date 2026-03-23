# core/risco.py

# Configurações iniciais (podem ser ajustadas depois)
LIMITE_PERDA = 200
META_LUCRO = 500

estado_risco = {
    "lucro_atual": 0,
    "perda_atual": 0
}

def atualizar_risco(valor_aposta, resultado):
    """
    Atualiza o lucro ou perda atual
    resultado: 'win' ou 'lose'
    """
    if resultado == "win":
        estado_risco["lucro_atual"] += valor_aposta
    elif resultado == "lose":
        estado_risco["perda_atual"] += valor_aposta

def verificar_limites():
    """
    Retorna True se o bot pode continuar jogando, False se atingiu limite
    """
    if estado_risco["perda_atual"] >= LIMITE_PERDA:
        return False
    if estado_risco["lucro_atual"] >= META_LUCRO:
        return False
    return True

def resetar_risco():
    estado_risco["lucro_atual"] = 0
    estado_risco["perda_atual"] = 0
