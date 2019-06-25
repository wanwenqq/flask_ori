from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False, unique=True) #unique表示必须是唯一的
    join_time = db.Column(db.DateTime, default=datetime.now )

    def __init__(self,phone,password,username):
        self.username = username
        self.password = password
        self.phone = phone

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result