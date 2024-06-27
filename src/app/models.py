from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    is_superuser=db.Column(db.Boolean,nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, user_id):
        self.email = email
        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'is_superuser':self.is_superuser,
            'create_time':  self.create_time,
            'update_time': self.update_time
        }