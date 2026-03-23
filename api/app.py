from flask import Flask
from flask_cors import CORS
from api.routes.entrada import entrada_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(entrada_bp)

if __name__ == "__main__":
    app.run(debug=True)
