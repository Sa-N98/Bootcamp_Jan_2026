from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # / == http://192.168.1.49:5001/
def home():
   
    return render_template("home.html")

@app.route('/explore') #  http://192.168.1.49:5001/explore
def explore():
    return render_template("explore.html")


@app.route('/my_bookings') #  http://192.168.1.49:5001/my_bookings
def my_bookings():
    return render_template("my_bookings.html")

app.run(debug=True, host='0.0.0.0', port=5001)