from .extensions import db


class Tools(db.Model):
    __tablename__ = "tool"
    box_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    is_borrowed = db.Column(db.Integer)
    user_id = db.Column(db.VARCHAR(255))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.name


class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100), unique=False)
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100), unique=False)
    phoneNumber = db.Column(db.VARCHAR(20), unique=False)
    isAllowed = db.Column(db.Integer, unique=False)

    def __init__(self, id, name, password, phoneNumber):
        self.name = name
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.isAllowed = 0  # 管理员审核是否可以批准

    def __repr__(self):
        return '<User %r>' % self.id


class Boxes(db.Model):
    __tablename__ = 'boxes'
    id = db.Column(db.Integer, primary_key=True)
    isEmpty = db.Column(db.Integer, unique=False)
    isWanted = db.Column(db.Integer, unique=False)
    usedPerson = db.Column(db.Integer, unique=False)
    wantedPerson = db.Column(db.Integer, unique=False)
    isActivity = db.Column(db.Integer, unique=False)

    def __init__(self, id, isActivity):
        self.id = id
        self.isEmpty = 0
        self.isWanted = 0
        self.usedPerson = 0
        self.wantedPerson = 0
        self.isActivity = isActivity

    def __repr__(self):
        return '<Box %r>' % self.id


class Powerbars(db.Model):
    __tablename__ = 'powerbars'
    id = db.Column(db.Integer, primary_key=True)
    isUsed = db.Column(db.Integer, unique=False)
    usedPerson = db.Column(db.Integer, unique=False)

    def __init__(self, id):
        self.id = id
        self.isUsed = 0
        self.usedPerson = 0

    def __repr__(self):
        return '<PowerBar %r>' % self.id


class Activities(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    maxmember = db.Column(db.Integer, unique=False)
    member = db.Column(db.Integer, unique=False)
    content = db.Column(db.String(256), unique=False)
    power_require = db.Column(db.Boolean, unique=False)
    tool_list = db.Column(db.String(64), unique=False)
    tool_box_start = db.Column(db.Integer, unique=True)

    def __init__(self, id, name, member, maxmember, content, power_require, tool_list, tool_box_start):
        self.id = id
        self.name = name
        self.content = content
        self.maxmember = maxmember
        self.member = member
        self.power_require = power_require
        self.tool_list = tool_list
        self.tool_box_start = tool_box_start

    def __repr__(self):
        return '<Activity %r>' % self.name