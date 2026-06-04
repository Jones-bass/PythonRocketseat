from flask import Flask
from src.models.settings.db_connection_handler import db_connection_handler

from src.main.routes.orders_routes import orders_routes_bp

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(orders_routes_bp)
