# Music Flask API Project

This Flask-based API allows users to interact with a music catalog.Users can retrieve a list of songs, search for tracks by title, and rate their favorite songs. The API ensures efficient data management and easy access for users to interact with the song catalog and submit ratings.

## Table of Contents
- [Installation](#installation)
- [Endpoints](#endpoints)
- [Run Test](#run-test)
---

## Installation

To get started, you need to set up the project environment and install the necessary dependencies.

### 1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/SwathySankaranarayanan/music_catalog.git
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
---
## Endpoints

### 1.GET /songs/

Fetch paginated list of songs.
```
curl -X GET http://localhost:5000/songs/?page=2&per_page=10
```

### 2. GET /songs/`<title>`
Fetch the song if available or else throws NotFound error
```
curl -X GET http://localhost:5000/songs/avreg
```
### 3. POST /songs/`<title>`
Adds the rating to the song if it is available , throws NotFound if the song is not available.If the rating is not with in 1 to 5 raises Value error
```
curl -X POST http://localhost:5000/songs/3AM -H "Content-Type: application/json" -d '{"rating": 4}'
```
### 4.POST /songs/
Sources the data from data_set.json to the table
```
curl -X POST http://localhost:5000/songs/
```
---

## Run Test
To run test case

```
pip install pytest
python -m pytest test/test_controller.py
```
