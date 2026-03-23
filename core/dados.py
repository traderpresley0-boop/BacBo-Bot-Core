# core/dados.py
from datetime import datetime

def validar_entrada(entrada):
    """
    Valida se a entrada é P ou B
    Retorna dicionário com valor e timestamp, ou None se inválido
    """
    entrada = entrada.upper()
    if entrada not in ["P", "B"]:
        return None
    return {"valor": entrada, "timestamp": datetime.now()}
