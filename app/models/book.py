from app import db
from sqlalchemy.orm import relationship

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'))
    