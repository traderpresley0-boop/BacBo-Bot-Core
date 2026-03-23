from core.dados import validar_entrada
from core.engine import processar_entrada
from core.risco import resetar_risco
from core.estado import estado
from config import settings

# Inicialização
resetar_risco()
estado["historico"].clear()
estado["total_jogadas"] = 0
estado["contagem"] = {"P":0,"B":0}
estado["sequencia_atual"] = {"tipo":None,"tamanho":0}

print(f"Bot iniciado! Banca inicial: {settings.BANCA_INICIAL}\n")

while True:
    entrada = input("Resultado (P/B) ou Q: ").strip().upper()

    if entrada == "Q":
        break

    resultado = validar_entrada(entrada)
    if not resultado:
        print("Entrada inválida\n")
        continue

    resposta = processar_entrada(resultado)

    print("\n--- RESULTADO ---")
    print(resposta)
    print("-----------------\n")

    if not resposta["risco"]["limites_ok"]:
        print("Limite atingido. Encerrando.")
        break
