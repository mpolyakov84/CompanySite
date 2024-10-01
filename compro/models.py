from datetime import datetime

from compro import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
    

class Users (db.Model, UserMixin):
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(64), nullable = False)
     email = db.Column(db.String(128), nullable=True, index=True, unique=True)
     hash_password = db.Column(db.String(128))
     profile_photo_path = db.Column(db.String(), default='default.jpg')
     post = db.relationship('Blogs', backref='author', lazy='dynamic')
     
     def __init__(self, username, email, password):
         self.username = username
         self.email = email
         self.hash_password = generate_password_hash(password)

     def check_pass(self, password):
            return check_password_hash(self.hash_password,password)

            
     def __repr__(self):
             return f'User {self.username}'

class Blogs(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, default = datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    def __repr__(self):
        return f'Blog {self.title}'

