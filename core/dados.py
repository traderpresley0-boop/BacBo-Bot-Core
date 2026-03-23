# core/dados.py
from datetime import datetime

def validar_entrada(entrada):
    entrada = entrada.upper()
    if entrada not in ["P", "B"]:
        return None

    return {
        "valor": entrada,
        "timestamp": datetime.now()
    }
