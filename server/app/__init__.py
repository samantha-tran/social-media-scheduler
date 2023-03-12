from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Blueprints
from .views.routes import api
from .views.instagram import instagram_api

def create_app(config_overrides=None):
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

    if config_overrides:
        app.config.update(config_overrides)
    
    # Load the models
    from app.models import db
    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()
        db.session.commit()
        
    # Routes related to core functionality
    api.register_blueprint(instagram_api)
    app.register_blueprint(api)

    # Routes related to instagram parsing
    return app