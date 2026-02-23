from flask import render_template, request
from model import *


def userdashbord(app):
    @app.route('/usrDashbord/<username>', methods=['GET', 'POST']) 
    def usrDashbord(username):
        movie_data = movies.query.all()
        user = User.query.filter_by(username=username).first()

        return render_template("user_dashbord.html", movies=movie_data, user=user)   

