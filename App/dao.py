from App import models
from App.models import Product, Category, User


def get_categories():
    return Category.query.all()


def get_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()


def get_user(user_id):
    return User.get.query(user_id)

