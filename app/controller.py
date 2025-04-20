from flask import Blueprint,current_app,request
from flask_restful import Api,Resource
import configparser
import os
from app.models import db,Song
from werkzeug.exceptions import BadRequest, NotFound,InternalServerError

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
song_blueprint = Blueprint('song',__name__,url_prefix='/songs')
song_api = Api(song_blueprint)

class Songs(Resource):
    def get(self):
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))
            # current_app.logger.info("before query ")
            pagination = Song.query.paginate(page=page, per_page=per_page, error_out=False)
            # current_app.logger.info("data %s",pagination)
            results = [song.to_dict() for song in pagination.items]

            return {
                'total': pagination.total,
                'pages': pagination.pages,
                'current_page': page,
                'per_page': per_page,
                'songs': results
            },200
        except Exception as e:
            raise InternalServerError("An error occurred while processing your request") from e

    def post(self):
        import json
        with open(config['DATABASE']['DATA_SET'], 'r') as f:
            data = json.load(f)
        rows = []
        # current_app.logger.info("data %s",data['id'])
        for i in range(len(data['id'])):  
            row={}
            for key in data:
                key_name = 'Class' if key == 'class' else key  
                row[key_name] = data[key][str(i)]
            rows.append(row)

        # Insert each row into the database
        for row in rows:
            current_app.logger.info("row %s",type(row))
            song = Song(**row)  # Create a Song object dynamically with the data in each row
            db.session.add(song)
        
        db.session.commit() 
        return {"message": "Song added successfully"}, 200

song_api.add_resource(Songs,'/')

class SongTrack(Resource):
    def get(self,title):
        song = Song.query.filter_by(title=title).first()
        if song:
            return song.to_dict()
        else:
            raise NotFound(f"Song with title '{title}' not found")
    
    def post(self,title):

        data = request.get_json()

        if not data or 'rating' not in data:
            raise BadRequest("Missing required field: 'rating'")
        
        rating = data.get("rating")

        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5')

        song = Song.query.filter_by(title=title).first()

        if not song:
            raise NotFound(f"Song with title '{title}' not found")

        song.rating = rating
        db.session.commit()

        return {
            'message': f"Rating updated to {rating} for song '{title}'",
            'song': song.to_dict()
        }, 200

song_api.add_resource(SongTrack,'/<string:title>')

