# logs/logger.py
from datetime import datetime

LOG_FILE = "logs/bot_logs.txt"

def registrar_entrada(resultado, pontuacao_total=None, padrao_forte=None):
    with open(LOG_FILE, "a") as f:
        log = f"[{datetime.now()}] Resultado: {resultado}"
        if pontuacao_total is not None and padrao_forte is not None:
            log += f" | Pontuação total: {pontuacao_total} | Padrão mais forte: {padrao_forte}"
        f.write(log + "\n")

def registrar_mensagem(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")
