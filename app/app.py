# coding=utf-8
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from .admin.views import admin
from .api import views as apiview
from .config import config
from .dev import views as devview
from .extensions import bootstrap, login_manager, babel
from .models import db


def create_app(config_name):
    sentry_sdk.init(
        dsn="https://5753772e9dc4470ba3881a0ea5426099@sentry.io/1318918",
        integrations=[FlaskIntegration()]
    )
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key = 'Simple'
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
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    babel.init_app(app)
    return None
