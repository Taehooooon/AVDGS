from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/gam")
def gam():
    return render_template("gam.html")

@app.route("/freetext")
def freetext():
    return render_template("freetext.html")

@app.route("/applytext")
def applytext():
    # gatenum = request.args.get("gate_num")
    inputtext = request.args.get("intext")
    # savedtext = request.args.get("saved_text")
    # return render_template("applytext.html")
    print(inputtext)
    print(inputtext)
    print(inputtext)
    print(inputtext)
    
@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=int(sys.argv[1]))
    app.run(debug=True)