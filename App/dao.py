from App import models
from App.models import Product, Category


def get_categories():
    return Category.query.all()


def get_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()


