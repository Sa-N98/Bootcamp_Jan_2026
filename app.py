from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # / == http://192.168.1.49:5001/
def home():
   
    return render_template("home.html")

@app.route('/explore', methods=['GET', 'POST']) #  http://192.168.1.49:5001/explore
def explore():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if '@' in email and '.' in email:
            print(f"\n\n\nUsername: {username}, Email: {email}, Password: {password}")
            return render_template("explore.html", username=username, email=email, password=password)
        else:
            print("\n\n\nInvalid email address. Please enter a valid email.")


    return render_template("explore.html")


@app.route('/my_bookings') #  http://192.168.1.49:5001/my_bookings
def my_bookings():
    return render_template("my_bookings.html")

app.run(debug=True, host='0.0.0.0', port=5001)