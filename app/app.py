from flask import Flask

from . import config
from .api import views as apiview


def create_app(config_object=config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """注册蓝图"""
    app.register_blueprint(apiview.blueprint)
    return None
