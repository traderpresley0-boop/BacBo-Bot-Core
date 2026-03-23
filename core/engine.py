from core.estado import atualizar_estado, estado
from core.estrategias import analisar_estrategias
from core.risco import atualizar_risco, verificar_limites, get_estado_risco
from config import settings
from logs.logger import registrar_entrada

def processar_entrada(resultado):
    # Atualiza estado
    atualizar_estado(resultado)

    # Estratégias
    analise = analisar_estrategias(estado["historico"])
    total_pontos = sum(item["pontos"] for item in analise)
    padrao_forte = max(analise, key=lambda x: x["pontos"])["tipo"] if analise else None

    # Risco
    atualizar_risco(settings.APOSTA_BASE, "win")
    limites_ok = verificar_limites()
    risco_estado = get_estado_risco()

    # Log
    registrar_entrada(resultado["valor"], total_pontos, padrao_forte)

    return {
        "historico": estado["historico"],
        "sequencia": estado["sequencia_atual"],
        "contagem": estado["contagem"],
        "pontos": total_pontos,
        "padrao_forte": padrao_forte,
        "estrategias": analise,
        "risco": {
            "banca": risco_estado["banca"],
            "lucro": risco_estado["lucro"],
            "perda": risco_estado["perda"],
            "limites_ok": limites_ok
        }
    }
