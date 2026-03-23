from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def criar_entrada():
    @app.route("/status")
    def status():
        return jsonify({"status": "BacBo Bot ativo"})

    app.run(port=5000)
