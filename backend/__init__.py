from flask import Flask
from flask_cors import CORS

from backend.app.database import db
from backend.config import Config
from backend.app.forums.models import Category, Post, Comment, PostLike, CommentLike
from backend.app.auth.models import User
from backend.app import api


def configure_database(app):
    @app.before_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_database(exception=None):
        db.session.remove()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins="http://localhost:5173")
    db.init_app(app)
    configure_database(app)
    api.init_app(app)

    return app