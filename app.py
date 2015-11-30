from flask import Flask, render_template, request, redirect, url_for
import util
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        query1 = request.form['querywho']
        query2 = request.form['querywhen']
        r1 =  util.getWhoResults(query1)
        print r1
        return redirect(url_for("result",result=r1))
                

@app.route("/result/<result>",)
def result(result=""):
    return render_template("result.html", result = result)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
