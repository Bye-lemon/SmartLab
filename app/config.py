import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SQLALCHEMY_DATABASE_URI = r'mysql://root:password@140.143.186.223:3306/GeZhiSpace'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
