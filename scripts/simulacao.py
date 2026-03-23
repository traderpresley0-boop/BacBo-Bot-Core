# scripts/simulacao.py
import random
from core.estado import atualizar_estado, estado
from core.estrategias import analisar_estrategias
from logs.logger import registrar_entrada
from config import settings

def simular_rodadas(n=20):
    for _ in range(n):
        resultado = random.choice(["P","B"])
        atualizar_estado({"valor":resultado})
        analise = analisar_estrategias(estado["historico"])
        total_pontos = sum(item["pontos"] for item in analise)
        padrao_forte = max(analise, key=lambda x: x["pontos"])["tipo"] if analise else None

        # Registra no log
        registrar_entrada(resultado, total_pontos, padrao_forte)

    print(f"Simulação de {n} rodadas finalizada. Logs gravados em logs/bot_logs.txt")
