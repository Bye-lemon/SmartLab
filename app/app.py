from flask import Flask

from .api import views as apiview
from .dev import views as devview
from .config import config
from .extensions import bootstrap


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key='Simple'
    app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024
    register_blueprints(app)
    register_extensions(app)
    return app


def register_blueprints(app):
    """注册蓝图"""
    app.register_blueprint(apiview.blueprint)
    app.register_blueprint(devview.blueprint)
    return None


def register_extensions(app):
    bootstrap.init_app(app)
    return None
