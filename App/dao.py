from App import models
from App.models import Product, Category, User
from App import app
import hashlib


def get_categories():
    return Category.query.all()


def get_products(kw, cate_id, page):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()


def count_products():
    return Product.query.count()


def get_user(user_id):
    return User.get.query(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode("utf-8")).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
