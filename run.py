import os

from app.app import create_app

app = create_app(config_name=os.getenv('FLASK_CONFIG', 'development'))
