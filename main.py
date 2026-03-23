from core.estado import atualizar_estado, estado
from core.dados import validar_entrada
from core.estatisticas import calcular_frequencia, detectar_rachas, detectar_alternancias
from core.estrategias import analisar_estrategias

def mostrar_estado():
    print("\n=== ESTADO ATUAL ===")
    print("Total jogadas:", estado["total_jogadas"])
    print("Contagem:", estado["contagem"])
    print("Sequência atual:", estado["sequencia_atual"])
    print("====================\n")

def mostrar_estatisticas():
    freq = calcular_frequencia(estado["historico"])
    rachas = detectar_rachas(estado["historico"])
    alternancias = detectar_alternancias(estado["historico"])
    
    print("=== ESTATÍSTICAS ===")
    print("Frequência:", freq)
    print("Rachas:", rachas)
    print("Alternâncias:", alternancias)
    print("====================\n")

def mostrar_estrategias():
    analise = analisar_estrategias(estado["historico"])
    
    if not analise:
        print("Nenhuma estratégia detectada ainda.\n")
        return

    # Calcula pontuação total
    total_pontos = sum(item["pontos"] for item in analise)
    
    # Identifica padrão mais forte
    padrao_forte = max(analise, key=lambda x: x["pontos"])
    
    print("=== ESTRATÉGIAS DETECTADAS ===")
    for item in analise:
        print(f"{item['tipo']} → Pontos: {item['pontos']} → Detalhes: {item['detalhes']}")
    
    print(f"\nPONTUAÇÃO TOTAL: {total_pontos}")
    print(f"Padrão mais forte: {padrao_forte['tipo']} → Pontos: {padrao_forte['pontos']}\n")
    print("==============================\n")

# Loop interativo de teste
while True:
    entrada = input("Resultado (P/B ou Q para sair): ").strip().upper()
    
    if entrada == "Q":
        print("Encerrando teste...")
        break

    resultado = validar_entrada(entrada)
    if not resultado:
        print("Entrada inválida. Use apenas P ou B.")
        continue

    atualizar_estado(resultado)
    
    # Mostrar estado, estatísticas e estratégias com pontuação
    mostrar_estado()
    mostrar_estatisticas()
    mostrar_estrategias()
