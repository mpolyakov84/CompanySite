from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.load_user
def load_user(iser_id):
    user = Users.query.get(user_id)
    return user
    
db = SQLAlchemy()
class Users (db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(64), nullable = False)
     email = db.Column(db.String(128), nullable=True, index=True)
     hash_password = db.Column(db.String(128))
     blog = db.Relationship('blog', backref='author')
     
     def __init__(self, username, email, password):
         pass
         
         
        def check_pass(self, password):
            pass
            
         def __repr__(self):
             pass
