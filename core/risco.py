estado_risco = {
    "banca": 0,
    "lucro": 0,
    "perda": 0
}

def resetar_risco():
    from config import settings
    estado_risco["banca"] = settings.BANCA_INICIAL
    estado_risco["lucro"] = 0
    estado_risco["perda"] = 0

def atualizar_risco(valor, resultado):
    if resultado == "win":
        estado_risco["banca"] += valor
        estado_risco["lucro"] += valor
    else:
        estado_risco["banca"] -= valor
        estado_risco["perda"] += valor

def verificar_limites():
    from config import settings
    if estado_risco["perda"] >= settings.LIMITE_PERDA:
        return False
    if estado_risco["lucro"] >= settings.META_LUCRO:
        return False
    return True

def get_estado_risco():
    return estado_risco
