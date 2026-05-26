from flask import Flask
from flask_cors import CORS

# importar blueprints
from src.main.routes.pessoa_fisica import pessoa_fisica_route_bp
from src.main.routes.pessoa_juridica import pessoa_juridica_route_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(pessoa_fisica_route_bp)
app.register_blueprint(pessoa_juridica_route_bp)
