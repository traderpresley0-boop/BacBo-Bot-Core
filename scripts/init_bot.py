# scripts/init_bot.py
from core.estado import estado
from core.risco import resetar_risco
from config import settings

def iniciar_bot():
    # Limpa histórico e estado
    estado["historico"].clear()
    estado["total_jogadas"] = 0
    estado["contagem"] = {"P":0,"B":0}
    estado["sequencia_atual"] = {"tipo":None,"tamanho":0}

    # Reseta risco
    resetar_risco()

    print(f"Bot iniciado! Banca inicial: {settings.BANCA_INICIAL}, Aposta base: {settings.APOSTA_BASE}")
