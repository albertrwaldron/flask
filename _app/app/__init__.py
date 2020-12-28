from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Instantiate globally accessible libraries
db = SQLAlchemy()

def create_app():
    '''Initialize application'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # Initialize plugins
    db.init_app(app)

    with app.app_context():
        # Include routes
        from . import routes
        # Create SQL tables for data models
        db.create_all()
        # Register Blueprints

        # Return flask app
        return app