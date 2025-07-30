from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/stuff')
def hello2():
    return "<p> This is where I'd keep the game <p/>"

