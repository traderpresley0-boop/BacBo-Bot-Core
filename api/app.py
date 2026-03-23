from flask import Flask
from api.routes.entrada import entrada_bp

app = Flask(__name__)

# Registrar rotas
app.register_blueprint(entrada_bp)

if __name__ == "__main__":
    app.run(debug=True)
