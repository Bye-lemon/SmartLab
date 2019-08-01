import datetime

from .extensions import db


class Activity(db.Model):
    __table__name = "activity"
    activity_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    is_abled = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(255))
    rest_number = db.Column(db.Integer)
    max_number = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    teacher = db.Column(db.VARCHAR(255))


class ActivityDetail(db.Model):
    __tabelname__ = "activity_detail"
    activity_detail_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.VARCHAR(255))
    day = db.Column(db.VARCHAR(255))
    activity_order = db.Column(db.VARCHAR(255))
    location = db.Column(db.VARCHAR(255))
    activity_id = db.Column(db.Integer)


class Manipulation(db.Model):
    __tablename__ = "manipulation"
    manipulation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.VARCHAR(255))
    time = db.Column(db.DateTime)
    function_type = db.Column(db.Integer)
    box_id = db.Column(db.Integer)


class Tool(db.Model):
    __tablename__ = "tool"
    box_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    is_borrowed = db.Column(db.Integer)
    user_id = db.Column(db.VARCHAR(255))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self):
        self.is_borrowed = 0


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.VARCHAR(255), primary_key=True)
    name = db.Column(db.VARCHAR(255))
    pwd_hash = db.Column(db.VARCHAR(255))
    avatar_hash = db.Column(db.VARCHAR(255))
    major = db.Column(db.VARCHAR(255))
    email = db.Column(db.VARCHAR(255), unique=True)
    is_allowed = db.Column(db.Integer)
    role = db.Column(db.Integer)
    coin = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    is_deleted = db.Column(db.Integer)
    verification_code = db.Column(db.VARCHAR(255))


class UserActivity(db.Model):
    __tablename__ = "user_activity"
    user_id = db.Column(db.VARCHAR(255), primary_key=True)
    activity_id = db.Column(db.Integer, primary_key=True)
    is_completed = db.Column(db.Integer)
    score = db.Column(db.Integer)
