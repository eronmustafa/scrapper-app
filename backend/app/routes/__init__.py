from flask import Blueprint
from .characters import characters_bp

# Blueprint for all routes
def register_routes(app):
    app.register_blueprint(characters_bp)
