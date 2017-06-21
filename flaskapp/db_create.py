from app import db

#create the database and the db tables
db.create_all()

#insert

#commit the change
db.session.commit()