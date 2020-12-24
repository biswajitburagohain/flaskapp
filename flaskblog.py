from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from passlib.hash import sha256_crypt
#import psycopg2
from pymongo import MongoClient
from psycopg2 import Error
from register import RegisterForm

app = Flask(__name__)
Articles = Articles()

@app.route("/") #this will be the initial page
def home():
    return render_template('home.html')

@app.route("/about") #this will take us to about page
def about():
    return render_template('about.html', title = 'About')

@app.route("/articles") #this will take us to about page
def article():
    return render_template('articles.html', articles = Articles)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.hash(str(form.password.data))

        client = MongoClient('localhost', 27017)
        collection = client['flaskblogdb']['flaskblog']
        doc = {'name': name, 'username': username, 'email': email, 'password': password}
        collection.insert_one(doc)        

        flash(message= 'User created successfully', category= 'success')
        return redirect(url_for('home'))

    return render_template('register.html', form = form)


if __name__ == "__main__":
    app.secret_key = 'secret_key'
    app.run(debug=True)