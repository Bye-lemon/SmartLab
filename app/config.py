import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SQLALCHEMY_DATABASE_URI = r'mysql+pymysql://yp:123@47.106.34.209:3306/laboratory'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    SECRET_KEY = "Simple"


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
