from flask import Flask, request, jsonify
from flask_cors import CORS
from core.engine import processar_entrada
from core.estado import estado
from core.risco import resetar_risco

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# Endpoint para enviar resultado P/B
@app.route("/entrada", methods=["POST"])
def entrada():
    data = request.get_json()
    resultado = data.get("resultado")
    if resultado not in ["P", "B"]:
        return jsonify({"error": "Entrada inválida, use apenas P ou B"}), 400

    resposta = processar_entrada({"valor": resultado})
    return jsonify(resposta)

# Endpoint para obter estado atual
@app.route("/estado", methods=["GET"])
def estado_atual():
    from core.risco import get_estado_risco
    estado_risco = get_estado_risco()
    return jsonify({
        "historico": estado["historico"],
        "sequencia": estado["sequencia_atual"],
        "contagem": estado["contagem"],
        "risco": {
            "banca": estado_risco["banca"],
            "lucro": estado_risco["lucro"],
            "perda": estado_risco["perda"],
            "limites_ok": estado_risco["perda"] < 2000 and estado_risco["lucro"] < 3000
        }
    })

# Endpoint para resetar o bot
@app.route("/reset", methods=["POST"])
def resetar():
    resetar_risco()
    estado["historico"].clear()
    estado["total_jogadas"] = 0
    estado["contagem"] = {"P":0,"B":0}
    estado["sequencia_atual"] = {"tipo":None,"tamanho":0}
    return jsonify({"status": "Bot resetado"})

if __name__ == "__main__":
    app.run(debug=True)
