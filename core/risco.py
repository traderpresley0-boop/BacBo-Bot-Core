from core.dados import validar_entrada
from core.estado import atualizar_estado, estado
from core.estrategias import analisar_estrategias
from core.risco import atualizar_risco, verificar_limites, resetar_risco
from config import settings

# Inicialização
resetar_risco()
estado["historico"].clear()
estado["total_jogadas"] = 0
estado["contagem"] = {"P":0,"B":0}
estado["sequencia_atual"] = {"tipo":None,"tamanho":0}

print(f"Bot iniciado! Banca inicial: {settings.BANCA_INICIAL}, Aposta base: {settings.APOSTA_BASE}\n")

while True:
    entrada = input("Resultado (P/B) ou Q para sair: ").strip().upper()
    if entrada == "Q":
        print("Encerrando bot...")
        break

    resultado = validar_entrada(entrada)
    if not resultado:
        print("Entrada inválida. Use apenas P ou B.\n")
        continue

    atualizar_estado(resultado)

    # Detectar estratégias
    analise = analisar_estrategias(estado["historico"])
    total_pontos = sum(item["pontos"] for item in analise)
    padrao_forte = max(analise, key=lambda x: x["pontos"])["tipo"] if analise else None

    # Atualizar risco (simulando aposta base)
    atualizar_risco(settings.APOSTA_BASE, "win")  # por enquanto assume vitória, depois poderá usar real
    limites_ok = verificar_limites()

    # Mostrar resultados
    print("\n--- ESTADO ATUAL ---")
    print("Histórico:", estado["historico"])
    print("Sequência atual:", estado["sequencia_atual"])
    print("Contagem:", estado["contagem"])
    print("--- ESTRATÉGIAS ---")
    for item in analise:
        print(f"{item['tipo']} → Pontos: {item['pontos']}")
    print(f"Pontuação total: {total_pontos}")
    print(f"Padrão mais forte: {padrao_forte}")
    print(f"Limites de risco ok? {'Sim' if limites_ok else 'Não'}")
    print("---------------------\n")
