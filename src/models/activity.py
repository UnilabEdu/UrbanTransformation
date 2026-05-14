from src.ext import db

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    DateTime = db.Column(db.String)
    Time = db.Column(db.Integer)
