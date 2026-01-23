from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String, Float, desc
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

import requests
import os
import ast


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = "FIX LATER"
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-project.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(254))
    password: Mapped[str] = mapped_column(String(100))
    watchlist: Mapped[List["Movie"]] = relationship(back_populates="user")

class Movie(db.Model):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    desc: Mapped[str] = mapped_column(String(1000))
    release_date: Mapped[str] = mapped_column(String(10))
    rating: Mapped[float] = mapped_column(Float)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="watchlist")




with app.app_context():
    db.create_all()
    example_user = User(email="example@gmail.com", password="12345", watchlist=[])

    ex_movie_1 = Movie(
        title="Sinners",
        desc="Awesome Vampire Movie",
        release_date="04-18-2025",
        rating= 10.0,
        user = example_user
    )
    ex_movie_2 = Movie(
        title="Weapons",
        desc="Scary Horror Movie",
        release_date="08-08-2025",
        rating= 9.5,
        user = example_user
    )
    db.session.add(example_user)
    db.session.commit()
    



@app.route("/")
def hello_world():
    
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)