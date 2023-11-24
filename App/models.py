from sqlalchemy import Column, Integer, String, Float, ForeignKey, BOOLEAN, Enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from App import app, db
from flask_login import UserMixin
import hashlib
import enum
import os


class UserRole(enum.Enum):
    USER = 1
    ADMIN = 2
    AGENT = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    # active = Column(BOOLEAN, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    messages = relationship("Message", backref="user", lazy=True)
    blogs = relationship("Blog", backref="user", lazy=True)

    def __str__(self):
        return self.name


class Message(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    k = Column(Integer)
    message = Column(String(100))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __str__(self):
        return self.name


class Blog(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(300))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    message_id = Column(Integer, ForeignKey(Message.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        r"""u1 = User(name="admin", username="admin",
                 password=str(hashlib.md5("123456".encode("utf-8")).hexdigest()),
                 user_role=UserRole.ADMIN)
        u2 = User(name="NASA", username="nasa",
                 password=str(hashlib.md5("123456".encode("utf-8")).hexdigest()),
                 user_role=UserRole.AGENT)
        db.session.add_all([u1, u2])
        m1 = Message(k=3, message="Found a teddy bear", user_id=2)
        b1 = Blog(title="Mastering Your Time Proven Strategies for Boosting Productivity",
                  content=r"C:\Users\Khanh\Desktop\SalesApp\App\blogs\Mastering Your Time Proven Strategies for Boosting Productivity.txt",
                  user_id=2, message_id=1)
        db.session.add_all([b1])
        db.session.commit()
        b2_filename = r"C:\Users\Khanh\Desktop\SalesApp\App\blogs\Embracing Mindfulness - A Guide to Cultivating a Present and Fulfilling Life.txt"
        b2 = Blog(title=os.path.splitext(os.path.basename(b2_filename))[0],
                  content=b2_filename,
                  user_id=1, message_id=1)
        b3_filename = r"C:\Users\Khanh\Desktop\SalesApp\App\blogs\The Lifelong Learning Advantage - Unlocking Your Full Potential.txt"
        b3 = Blog(title=os.path.splitext(os.path.basename(b3_filename))[0],
                  content=b3_filename,
                  user_id=1, message_id=1)
        db.session.add_all([b2, b3])
        db.session.commit()"""
