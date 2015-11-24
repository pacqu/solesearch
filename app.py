from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("search.html")

@app.route("/", methods = ["POST"])
def index2():
    query1 = request.form['query1']
    query2 = request.form['query2']
    query3 = request.form['query3']
    #util.
    return 0

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
