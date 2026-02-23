from flask import Flask, render_template, request
from model import *
from routes.login import userLogin
from routes.signup import userSignup
from routes.dashbord import userdashbord
import os

app = Flask(__name__)

current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(current_dir, 'movie_booking.db')

db.init_app(app)
app.app_context().push()

@app.route('/') # / == http://192.168.1.49:5001/
def landing():
    return render_template("landing.html")


@app.route('/theater_onbording', methods=['GET', 'POST'])
def theater_onbording():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        movies_list = request.form['movies'].split(',')  # Get list of selected movies

        if not name or not location:
            return "Name and location are required!", 400
        if not movies_list:
            return "At least one movie must be selected!", 400
        if theaters.query.filter_by(name=name).first():
            return "Theater with this name already exists!", 400
        
        theater = theaters(name=name, location=location)
        db.session.add(theater)
        db.session.flush()
        print(theater.id)
        for movie_title in movies_list:
            movie = movies.query.filter_by(title=movie_title).first()
            if not movie:
                new_movie = movies(title=movie_title)
                
                db.session.add(new_movie)
                db.session.flush()
                print(new_movie.id)
                association = movie_theaters(movie_id=new_movie.id, theater_id=theater.id)
                db.session.add(association)
        
        
        db.session.commit()

        return "Theater added successfully!", 201
    return render_template("theater_onbording.html")

userLogin(app)
userSignup(app)
userdashbord(app)

def cread_admin():

    if User.query.filter_by(username='admin').first():
        return "Admin user already exists!"
    
    admin = User(username='admin', email='admin@email.com', password='admin123', type='admin')
    db.session.add(admin)
    db.session.commit()



if __name__ == '__main__':
    db.create_all()
    cread_admin()
    app.run(debug=True, host='0.0.0.0', port=5001)