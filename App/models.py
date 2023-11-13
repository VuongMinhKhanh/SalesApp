from sqlalchemy import Column, Integer, String, Float, ForeignKey, BOOLEAN
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from App import app, db
from flask_login import UserMixin
import hashlib

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(BOOLEAN, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)


class Category(db.Model):
    # __tablename__ = 'category’
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)  # để product va category trong "" vì py thông dịch, khi nào thấy class rồi mới lấy lên

    def __str__(self):
        return self.name


class Product(db.Model):
    # __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100),
                   default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(BOOLEAN, default=True)
    category_id = Column(Integer,
                         ForeignKey(Category.id), nullable=False)
    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()#
        u = User(name="admin", username="admin", active=True, password=str(hashlib.md5("123456".encode("utf-8")).hexdigest()))
        db.session.add(u)
        db.session.commit()
        """c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Bphone")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()
        p1 = Product(name="Iphone 20", price=20000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        p2 = Product(name="Galaxy 20", price=20000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=2)
        p3 = Product(name="Iphone 20", price=20000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        p4 = Product(name="Galaxy 20", price=20000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=2)
        p5 = Product(name="Iphone 20", price=20000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
                     category_id=1)
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.commit()"""
