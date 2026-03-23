# scripts/init_bot.py
from core.estado import estado
from config import settings
from core.risco import resetar_risco, estado_risco

def iniciar_bot():
    """
    Inicializa o bot:
    - limpa histórico
    - reseta sequências
    - reseta risco
    """
    estado["historico"].clear()
    estado["total_jogadas"] = 0
    estado["contagem"] = {"P": 0, "B": 0}
    estado["sequencia_atual"] = {"tipo": None, "tamanho": 0}
    
    # Atualiza risco usando configurações globais
    estado_risco["lucro_atual"] = 0
    estado_risco["perda_atual"] = 0
    
    print(f"Bot iniciado! Banca inicial: {settings.BANCA_INICIAL}, Aposta base: {settings.APOSTA_BASE}")
