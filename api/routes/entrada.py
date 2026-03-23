from flask import Blueprint, request, jsonify

from core.estado import atualizar_estado, estado
from core.estrategias import analisar_estrategias
from core.risco import atualizar_risco, verificar_limites, get_estado_risco
from core.dados import validar_entrada
from config import settings
from logs.logger import registrar_entrada

entrada_bp = Blueprint("entrada", __name__)

@entrada_bp.route("/entrada", methods=["POST"])
def entrada():
    data = request.get_json()

    if not data or "resultado" not in data:
        return jsonify({"erro": "Campo 'resultado' é obrigatório"}), 400

    entrada = data["resultado"].upper()

    resultado = validar_entrada(entrada)
    if not resultado:
        return jsonify({"erro": "Entrada inválida. Use P ou B"}), 400

    # Atualiza estado
    atualizar_estado(resultado)

    # Estratégias
    analise = analisar_estrategias(estado["historico"])
    total_pontos = sum(item["pontos"] for item in analise)
    padrao_forte = max(analise, key=lambda x: x["pontos"])["tipo"] if analise else None

    # Risco (simulação inicial: sempre win)
    atualizar_risco(settings.APOSTA_BASE, "win")
    limites_ok = verificar_limites()
    risco_estado = get_estado_risco()

    # Log
    registrar_entrada(resultado["valor"], total_pontos, padrao_forte)

    # Resposta estruturada
    resposta = {
        "historico": estado["historico"],
        "sequencia": estado["sequencia_atual"],
        "contagem": estado["contagem"],
        "pontos": total_pontos,
        "padrao_forte": padrao_forte,
        "estrategias": analise,
        "risco": {
            "banca_atual": risco_estado["banca"],
            "lucro": risco_estado["lucro"],
            "perda": risco_estado["perda"],
            "limites_ok": limites_ok
        }
    }

    return jsonify(resposta)
