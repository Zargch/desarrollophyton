from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    nacionalidad = db.Column(db.String(255), nullable=False)
   
