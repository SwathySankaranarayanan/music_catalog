import sys
import os
import pytest
import json
from app import create_app
from app.models import db,Song
@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            song = Song(id="pefon34321",title="Test Song 1")
            db.session.add(song)
            song = Song(id="mvkregn",title="Rock and Roll")
            db.session.add(song)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()


def test_get_songs(client):
    response = client.get('/songs/?page=1&per_page=1')
    data = response.get_json()
    assert response.status_code == 200
    assert data['songs']==[{'id': 'pefon34321', 'title': 'Test Song 1', 'danceability': None, 'energy': None, 'key': None, 'loudness': None, 'mode': None, 'acousticness': None, 'instrumentalness': None, 'liveness': None, 'valence': None, 'tempo': None, 'duration_ms': None, 'time_signature': None, 'num_bars': None, 'num_sections': None, 'num_segments': None, 'Class': None, 'rating': None}]

def test_rate_unavailable_song(client):
    response = client.post(
        'http://localhost:5000/songs/3AM',
        json={"rating": 4}
    )
    assert response.status_code == 404

def test_rate_song(client):
    response = client.post(
        'http://localhost:5000/songs/Rock and Roll',
        json={"rating": 4}
    )
    # breakpoint()
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['message'] == "Rating updated to 4 for song 'Rock and Roll'"


def test_get_unavailable_song(client):
    response = client.get(
        'http://localhost:5000/songs/3AM',
    )
    assert response.status_code == 404

def test_get_song(client):
    response = client.get(
        'http://localhost:5000/songs/Rock and Roll',
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data == {'id': 'mvkregn', 'title': 'Rock and Roll', 'danceability': None, 'energy': None, 'key': None, 'loudness': None, 'mode': None, 'acousticness': None, 'instrumentalness': None, 'liveness': None, 'valence': None, 'tempo': None, 'duration_ms': None, 'time_signature': None, 'num_bars': None, 'num_sections': None, 'num_segments': None, 'Class': None, 'rating': None}





