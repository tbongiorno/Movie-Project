#Flask
from flask import Flask, flash, redirect, render_template, request, url_for, session

#SQL
import flask_sqlalchemy
from sqlalchemy import ForeignKey, Integer, String, Float, desc
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

#User Manager
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

#Design imporst
from flask_bootstrap import Bootstrap5

#misc imports
import requests
from dotenv import load_dotenv
import os

#Starting File for Movie Project
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)