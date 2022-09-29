from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import pandas as pd

app = Flask(__name__)

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    git
    init
    git
    add
    README.md
    git
    commit - m
    "first commit"
    git
    branch - M
    main
    git
    remote
    add
    origin
    https: // github.com / arofre / recipe - searcher.git
    git
    push - u
    origin
    main
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def get_random_recipe():
    inp = list(request.form['content'])
    string = ""
    for i in inp:
        string += i.replace(" ", "")

    lst = string.split(",")

    df = pd.read_excel('recept.xlsx')
    recipe_dict = {}

    for i in lst:
        df = df[df['Ingredienser'].str.contains(i)]
    rec = df['Recept'].tolist()
    ing = df['Ingredienser'].tolist()

    for i,e in enumerate(rec):
        recipe_dict[e] = ing[i]

    recipe, ingredients = random.choice(list(recipe_dict.items()))

    return redirect(recipe, code=302)

if __name__ == "__main__":
    app.run(debug=True)