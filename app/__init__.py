from flask import Flask
from config import config_options

def create_app(config_name):
    app = Flask(__name__,instance_relative_config = True,static_url_path='/static')
    app.config.from_object(config_options[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .news_requests import configure_request
    configure_request(app)

    return app