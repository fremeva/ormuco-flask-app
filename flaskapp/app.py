from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Create the Sqlalchemy Object
db = SQLAlchemy(app)

# My Models
from models import *


@app.route("/", methods=['GET', 'POST'])
def index():
    error = None
    isOk = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            color = request.form['color']
            pet = request.form['pet']
            if (name and color and pet):
                # save data
                db.session.add(UserModel(str(name).upper(), color, pet))
                db.session.commit()
                isOk = 'Save Data! :)'
                error = None
            else:
                error = 'All fields are required. Please try again'
        except exc.IntegrityError as err:
            db.session.rollback() #Exception Rollback database
            error = err.message
        except Exception as e:
            error = e.message
        finally:
            db.session.close() #close session Database

    users = db.session.query(UserModel).all()
    return render_template('index.html', users=users, title='Flask App', error=error, isOk = isOk);


if __name__ == '__main__':
    app.run(debug=True)