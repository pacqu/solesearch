from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def index2(errors=""):
    r = ""
    print "\n\n\n"
    print request.form['querywhen']
    query1 = request.form['querywho']
    query2 = request.form['querywhen']
    query3 = request.form['querywhere']
    if query1 == None and query2 == None and query3 == None:
        errors = "Please fill one of the fields."
        return render_template("index.html", errors = errors)
    #If you enter something but click the wrong button -> error
    elif 'submitWho' in request.POST and query1 == None:
        errors = "Please enter a who query"
        return render_template("index.html", errors = errors)
    
    elif 'submitWhen' in request.POST and query2 == None:
        errors = "Please enter a when query"
        return render_template("index.html", errors = errors)

    elif 'submitWhere' in request.POST and query3 == None:
        errors = "Please enter a where query"
        return render_template("index.html", errors = errors)
    else:
        print "in else"
        if query1:
            r = query1
        elif query2:
            r = query2
        elif query3:
            r = query3
    print r
    return render_template("result.html",result = r)

@app.route("/result")
def about():
    return render_template("result.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
