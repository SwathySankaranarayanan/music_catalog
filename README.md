# Song track Flask API Project

This Flask-based API allows users to interact with a music catalog.Users can retrieve a list of songs, search for tracks by title, and rate their favorite songs. The API ensures efficient data management and easy access for users to interact with the song catalog and submit ratings.

## Table of Contents
- [Installation](#installation)
- [Endpoints](#endpoints)
---

## Installation

To get started, you need to set up the project environment and install the necessary dependencies.

### 1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/your-repo-name.git
cd song_track
```

### 2. Set up

Create virtual environment , activate and add the requirements  using 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

to start app
python main.py
```

### 3.Database

```
cd instance
sqlite3 songs.db

```
initial sourcing from data set

```
curl -X POST http://localhost:5000/songs/
curl -X POST http://localhost:5000/songs/3AM -H "Content-Type: application/json" -d '{"rating": 6}'
curl -X GET http://localhost:5000/songs/avreg
curl -X GET http://localhost:5000/songs/?page=2 

```
