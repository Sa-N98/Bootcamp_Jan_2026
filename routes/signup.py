from flask import render_template, request, redirect, url_for
from model import *


def userSignup(app):
    @app.route('/usrSignup', methods=['GET', 'POST']) 
    def usrSignup():
        if request.method == 'POST':
            # Handle form submission here
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            type = request.form["usr_type"]

            if not username or not email or not password:
                return "All fields are required!", 400
            if '@' not in email or '.' not in email:
                return "Invalid email address!", 400
            if User.query.filter_by(username=username).first():
                return "Username already exists!", 400
            if User.query.filter_by(email=email).first():
                return "Email already exists!", 400
            

            new_user = User(username=username, email=email, password=password, type=type)

            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('usrLogin'))
        return render_template("usr_signup.html")


