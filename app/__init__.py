from flask import Flask,Blueprint, jsonify
from app.models import db,Song
from app.routes import register_routes
from app.controller import song_blueprint
from app.error_handler import register_error_handlers
import os
import configparser
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

import logging



def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DATABASE']['SQLALCHEMY_TRACK_MODIFICATIONS']
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    db.init_app(app)

    register_routes(app)
    register_error_handlers(app)

    with app.app_context():
        db.create_all() 
        
    return app
