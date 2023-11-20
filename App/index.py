import math

from flask import render_template, request, redirect
import dao
from App import app, login
from App import admin
from App.models import User
from flask_login import login_user


@app.route("/")
def home():
    kw = request.args.get("kw")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")

    data = dao.get_categories()
    prods = dao.get_products(kw, cate_id, page)

    num = dao.count_products()
    page_size = app.config["PAGE_SIZE"]
    return render_template("index.html", cat=data, products=prods, pages=math.ceil(num/page_size))


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


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/admin/login", methods=["post"])
def login_admin():
    username = request.form.get("username")
    password = request.form.get("password")

    user = dao.auth_user(username=username, password=password)

    if user:
        login_user(user)

    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)
