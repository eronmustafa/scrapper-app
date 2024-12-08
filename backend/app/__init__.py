from flask import Flask
from flask_cors import CORS
from app.routes.characters import characters_bp
from app.db import get_db_pool
import asyncio

async def create_app():
    app = Flask(__name__)
    CORS(app)

    # Set up the database connection pool
    app.config['DB_POOL'] = await get_db_pool()

    # Register blueprints
    app.register_blueprint(characters_bp)

    # Define the default route
    @app.route('/')
    def home():
        return "Welcome to the Character API! Use the `/characters` endpoint to interact with data."

    return app
