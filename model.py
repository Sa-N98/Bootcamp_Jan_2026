from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)    


class movies (db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    poster = db.Column(db.String(), nullable=True)
    theaters_list = db.relationship('theaters', secondary='movie_theaters', backref='movies')

class movie_theaters (db.Model):
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, primary_key=True)
    theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'), nullable=False, primary_key=True)


class theaters (db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    movie_list = db.relationship('movies', secondary='movie_theaters', backref='theaters')