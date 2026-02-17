from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # / == http://192.168.1.49:5001/
def home():
    return render_template("home.html")

@app.route('/explore') #  http://192.168.1.49:5001/explore
def explore():
    return render_template("explore.html")

app.run(debug=True, host='0.0.0.0', port=5001)