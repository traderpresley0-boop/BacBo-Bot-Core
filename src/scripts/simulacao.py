from src.core.engine import Engine

def simular_rodadas(qtd=5):
    bot = Engine()
    for i in range(qtd):
        print(f"\n--- Rodada {i+1} ---")
        bot.rodar()

if __name__ == "__main__":
    simular_rodadas(10)
