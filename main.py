# main.py

from core.estado import atualizar_estado, estado
from core.dados import validar_entrada

def mostrar_estado():
    print("\n=== ESTADO ATUAL ===")
    print("Total:", estado["total_jogadas"])
    print("Contagem:", estado["contagem"])
    print("Sequência:", estado["sequencia_atual"])
    print("====================\n")

while True:
    entrada = input("Resultado (P/B): ")
    resultado = validar_entrada(entrada)
    
    if not resultado:
        print("Entrada inválida")
        continue

    atualizar_estado(resultado)
    mostrar_estado()
