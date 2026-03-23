# core/risco.py
from config import settings

estado_risco = {
    "lucro_atual": 0,
    "perda_atual": 0
}

def atualizar_risco(valor_aposta, resultado):
    if resultado=="win":
        estado_risco["lucro_atual"] += valor_aposta
    elif resultado=="lose":
        estado_risco["perda_atual"] += valor_aposta

def verificar_limites():
    if estado_risco["perda_atual"] >= settings.LIMITE_PERDA:
        return False
    if estado_risco["lucro_atual"] >= settings.META_LUCRO:
        return False
    return True

def resetar_risco():
    estado_risco["lucro_atual"] = 0
    estado_risco["perda_atual"] = 0
