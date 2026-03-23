from flask import Blueprint, request, jsonify
from core.dados import validar_entrada
from core.engine import processar_entrada

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

    # 🔥 Aqui está a diferença profissional
    resposta = processar_entrada(resultado)

    return jsonify(resposta)
