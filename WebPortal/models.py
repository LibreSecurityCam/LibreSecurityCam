from WebPortal import db, loginMan
from flask_login import UserMixin

@loginMan.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model, UserMixin):
    id = db.Column("id", db.Integer, primary_key = True, nullable = False)
    username = db.Column("username", db.String(50), unique=True, nullable = False)
    password = db.Column("password", db.String(100), unique=True, nullable = False)
    profilePicture = db.Column("profilePicture", db.String(20), nullable = False, default='default.png')
    isAdmin = db.Column("isAdmin", db.Boolean, nullable = False, default = False)


    def __init__(self, username, password, isAdmin):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

