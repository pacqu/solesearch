from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def index2():
    r = ""
    query1 = request.form['querywho']
    query2 = request.form['querywhen']
    query3 = request.form['querywhere']
    if not query1 or not query2 or not query3:
        errors = "Please fill one of the fields."
        return render_template("index.html",errors = errors)
    else:
        if query1:
            r = query1
        elif query2:
            r = query2
        elif query3:
            r = query3
    return render_template("result.html",result = r)

@app.route("/result/<result>")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
