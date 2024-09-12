from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/random_forest_regressor_42.sav", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["CRIM"])
        val2 = float(request.form["RM"])
        val3 = float(request.form["DIS"])
        val4 = float(request.form["LSTAT"])
        
        data = [[val1, val2, val3, val4]]
        prediction = int(model.predict(data)[0])
        
    else:
        prediction = None
    
    return render_template("index.html", prediction = prediction)