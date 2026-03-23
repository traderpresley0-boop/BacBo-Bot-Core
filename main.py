from src.core.engine import Engine
from src.config.settings import CONFIG
from src.api.entrada import criar_entrada

def main():
    print("Iniciando BacBo Bot...")
    bot = Engine()
    bot.start()
    criar_entrada()

if __name__ == "__main__":
    main()
