from flask import Flask, render_template, request, session
from flask_session import Session
import pypokedex
import random
import csv as csv

app = Flask(__name__)

# app.config['SECRET_KEY'] = "some_random"
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SESSION_PERMANENT']= False

# Session(app)


# TODO: 
# High Scores
# Look Nice
#


#should make class
field_names = ['ID', 'SCORE']

USER_NAME = ""

def log_scores(score):
    with open('scores.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(score)

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
    if request.method == 'POST':
        name = request.form['name']
        print(f'form: {name}')
        # session["name"], 
        USER_NAME = name
   
    # print(p.abilities)
    # print(p.get_descriptions)
    return render_template("index.html",user_image=filename,poke_name=p.name)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    max_score = request.form['javascript_data']
    print(f"{USER_NAME} highest score: {max_score}")
    # session['max_score'] = max_score
    log_scores([USER_NAME, max_score])
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
    app.run()