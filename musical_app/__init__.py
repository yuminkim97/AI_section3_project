from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__) # name = folder 이름

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config["ENV"] == 'development':
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app) # db와 app연결
    migrate.init_app(app, db)

    from musical_app.routes import (main_route, theater_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(theater_route.bp, url_prefix='/api')

    return app

if __name__ == "main":
    app = create_app()
    app.run(debug=True)


