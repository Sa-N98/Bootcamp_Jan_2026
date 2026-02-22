from flask import render_template, request
from model import *


def userLogin(app):
    @app.route('/usrLogin', methods=['GET', 'POST']) 
    def usrLogin():
        if request.method == 'POST':
            # Handle form submission here
            email = request.form["email"]
            password = request.form["password"]

            if "@" not in email or "." not in email:
                return "Invalid email address!", 400
            
            user = User.query.filter_by(email=email).first()
            if not user or user.password != password:
                return "Invalid email or password!", 400
            
            return f"Welcome back, {user.username}!"

        return render_template("usr_login.html")


