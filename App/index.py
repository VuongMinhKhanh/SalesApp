from flask import render_template, request
import dao
from SalesApp.App import app


@app.route("/")
def home():
    kw = request.args.get("kw")
    data = dao.get_categories()
    prods = dao.get_products(kw)

    return render_template("index.html", cat=data, products=prods)


@app.route("/test")
def test():
    return "Test con cac"


# path params
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html",
                           message="Xin chao %s" % name)


# number only
@app.route("/number/<int:num>")
def number(num):
    return render_template("index.html",
                           message="So de^` %d !!!" % num)


# ?params
@app.route("/hello")
def hello2():
    fn = request.args["first_name"]
    ln = request.args["last_name"]

    return render_template("index.html",
                           message="Xin chao %s %s" % (fn, ln))


if __name__ == "__main__":
    app.run(debug=True)