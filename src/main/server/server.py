from flask import Flask
from src.main.routes.tags_routes import tags_route_bp

app = Flask(__name__)

app.register_blueprint(tags_route_bp)
