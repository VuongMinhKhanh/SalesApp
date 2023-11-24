import math
from flask import render_template, request, redirect
import dao
from App import app, login
from App import admin
from App.models import User
from flask_login import login_user, current_user, UserMixin, AnonymousUserMixin


def display_content(file_path):
    with open(file_path, 'r') as file:
        file_content = file.readlines()
        file_content = " ".join(file_content)
        file.close()

    return file_content


def content_list(blog):
    return display_content(blog[0].content)


@app.route("/")
def home():
    blogs = dao.get_all_blogs()

    num = dao.count_blogs()
    page_size = app.config["PAGE_SIZE"]
    return render_template("index.html", blogs=blogs, contents=content_list(blogs),
                           pages=math.ceil(num/page_size), current_user=current_user)


@app.route("/decode")
def decode():
    blog_id = request.args.get("blog")

    return render_template("decode.html",
                           content=content_list(dao.get_blog(blog_id)))


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
