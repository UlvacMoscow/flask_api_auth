from flask_secutiry import UserMixin
import sqlite3


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    age = db.Column(db.Integer())

    def find_by_username(self, )
