from flask import Flask, render_template, request
from model import *
from routes.login import userLogin
from routes.signup import userSignup
import os

app = Flask(__name__)

current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(current_dir, 'users.db')

db.init_app(app)
app.app_context().push()

@app.route('/') # / == http://192.168.1.49:5001/
def landing():
    return render_template("landing.html")

userLogin(app)
userSignup(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)