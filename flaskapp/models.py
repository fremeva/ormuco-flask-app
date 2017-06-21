from app import db

class UserModel(db.Model):

    __tablename__ = "users"

    name = db.Column(db.String, primary_key=True, unique=True)
    color = db.Column(db.String, nullable=False)
    pet = db.Column(db.String, nullable=False)

    def __init__(self, name, color, pet):
        self.name = name
        self.color = color
        self.pet = pet