from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import pypokedex
import random
import csv as csv

app = Flask(__name__)
app.secret_key = "pokemon"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFCATIONS'] = False
# app.config['SECRET_KEY'] = "some_random"
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SESSION_PERMANENT']= False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    high_score = db.Column(db.Integer)

    def __init__(self, username, high_score):
        self.username = username
        self.high_score = high_score

# TODO: 
# High Scores
# Look Nice
#


#should make class
@app.route('/', methods=['GET', 'POST'])
def index():
    user = request.args.get("name")
    print(f'get: {user}')
    return render_template("username.html")

@app.route('/username', methods= ['POST'])
def get_username():
    name = request.form['username']
    print(f'form: {name}')
    return name


@app.route('/game', methods = ['GET', 'POST'])
def game():
    r = random.randint(1,251)
    filename = '/static/other/official-artwork/' + str(25) + '.png'
    p=pypokedex.get(dex=25)
    name = "PLACEHOLDER"
    if request.method == 'POST':
        name = request.form['name']
        session["name"] = name
    USER_NAME = users.query.with_entities(users.username).all()
    USER_SCORES = users.query.with_entities(users.high_score).all()
    names = [_users[0] for _users in USER_NAME]
    scores = [_scores[0] for _scores in USER_SCORES]
    return render_template("index.html",
        user_image=filename,
        poke_name=p.name, 
        usernames=names, 
        userscores=scores
    )

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():     #NEED TO RENAME VARIABLE 
    max_score = request.form['javascript_data']
    # session["max_score"] = max_score
    usr = users(session["name"], max_score)
    db.session.add(usr)
    db.session.commit()
    USER_NAME = users.query.with_entities(users.username).all()
    for _users in USER_NAME:
        print(_users[0])
    return max_score

@app.route('/pokename', methods = ['GET', 'POST'])
def get_name():
    message = {}
    if request.method == 'GET':
        r = random.randint(1,251)
        p=pypokedex.get(dex=r)
        message = {
            'pokename': p.name,
            'pokenum': r
        }
        
    return message


@app.route('/get_score', methods = ['POST'])
def get_score(): 
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()