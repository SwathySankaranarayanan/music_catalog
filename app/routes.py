from app.controller import song_blueprint
    
def register_routes(app):
    app.register_blueprint(song_blueprint)