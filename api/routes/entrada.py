from flask import Blueprint, request, jsonify
from core.dados import validar_entrada
from core.engine import processar_entrada

entrada_bp = Blueprint("entrada", __name__)

# 🔹 POST /entrada
@entrada_bp.route("/entrada", methods=["POST"])
def entrada():
    data = request.get_json()

    if not data or "resultado" not in data:
        return jsonify({"erro": "Campo 'resultado' é obrigatório"}), 400

    entrada = data["resultado"].upper()

    resultado = validar_entrada(entrada)
    if not resultado:
        return jsonify({"erro": "Entrada inválida. Use P ou B"}), 400

    resposta = processar_entrada(resultado)

    return jsonify(resposta)


# 🔹 GET /estado
@entrada_bp.route("/estado", methods=["GET"])
def estado_atual():
    from core.estado import estado
    from core.risco import get_estado_risco

    return jsonify({
        "historico": estado["historico"],
        "sequencia": estado["sequencia_atual"],
        "contagem": estado["contagem"],
        "risco": get_estado_risco()
    })


# 🔹 POST /reset
@entrada_bp.route("/reset", methods=["POST"])
def reset():
    from core.estado import estado
    from core.risco import resetar_risco

    estado["historico"].clear()
    estado["contagem"] = {"P":0,"B":0}
    estado["sequencia_atual"] = {"tipo":None,"tamanho":0}

    resetar_risco()

    return jsonify({"msg": "resetado"})
