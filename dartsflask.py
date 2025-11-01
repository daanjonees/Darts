from flask import Flask, render_template, request, session, redirect, url_for 
from collections import deque
import pickle

class Players:
    def __init__(player, name, score):
        player.name = name
        player.score = score

app = Flask(__name__)
app.secret_key = "dev"  

def can_checkout(rem):
    return bool((rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/playerdetails', methods=['POST'])
def playerdetails():
    session["remaining"] = int(request.form["starting_score"])
    session["numplayers"] = request.form["numplayers"]
    playerstring = ""

    for player in range(0, int(session["numplayers"])):
            playerstring = playerstring + '<h2>Enter player ' + str(player + 1) + ' name </h2> ' + \
                    '<input type="text" name="playernames[]" step="any" required> <br><br>' 
                    
                    
    return '<!DOCTYPE html> \
                <html> \
                <head> \
                <title>Player Details</title> \
                </head> \
                <body> \
                <h1> Setting up Players </h1> \
                \
                <form action="/loop" method="POST"> \
                <p> ' + playerstring + '</p> \
                <button type="submit">Submit</button> \
                </form> \
                 \
                <p>Do you want to start again? \
                <a href="http://127.0.0.1:5000/input"> \
                 \
                <button>Start</button> \
                    </a> </p> \
                </body> \
                </html>'

@app.route('/loop', methods=['GET', 'POST'])
def loop(): 
    playernames = request.form.getlist("playernames[]")
    if playernames != []:
        storedplayers = []
        for x in playernames:
            play = Players(str(x), session["remaining"])
            storedplayers.append(play)
        playername = storedplayers[0].name
        playerscore = storedplayers[0].score
        session["storedplayers"] = pickle.dumps(storedplayers)
    
    else:
        storedplayers = pickle.loads(session["storedplayers"])
        alterstoredplayers = deque(storedplayers)
        alterstoredplayers.rotate(-1)
        storedplayers = list(alterstoredplayers)
        playername = storedplayers[0].name
        playerscore = storedplayers[0].score 

        #if newscore != "":
        newscore = int(request.form["newscore"])

        if newscore - playerscore == 1:
            playerscore = playerscore
            session["storedplayers"] = pickle.dumps(storedplayers)
            
        if playerscore > newscore:
            playerscore -= newscore
            session["storedplayers"] = pickle.dumps(storedplayers)

        if newscore > playerscore:
            playerscore = playerscore
            session["storedplayers"] = pickle.dumps(storedplayers)

        if newscore == playerscore:
            #unsure what to do here? Redirect to start?
            session["storedplayers"] = pickle.dumps(storedplayers)

#if I add it outside do I need to pickle things inside the if statement? Or re-pickle.
#When is the best place to load in newscore? If I add it at the start will it error before the if loop.
    

##Write down each player and see how it works. 
    #has_changed = False

    #for x in storedplayers:
    #    if has_changed == True and x.status == False:
    #        x.status = True
    #        has_changed = False
    #    if x.status == True:
     #       playername = x.name
    #        playerscore = x.score
     #       x.status = False
     #       has_changed = True

##What happens when you get to the last player


    return '<!DOCTYPE html> \
            <html> \
            <head> \
            <title>Game Screen</title> \
            </head> \
            <body> \
            <h1> Game Loop </h1> \
            \
            <p> ' + playername + '</p> \
            \
            <p> ' + str(playerscore) + '</p> \
            <p> ' + str(storedplayers) + '</p> \
            \
            <p> What is your score? </p> \
            <form action="/loop" method="POST"> \
            \
            <input type="number" name="newscore" step="any" required>\
            \
            <button type="submit">Submit</button> \
            </form> \
            <p>Do you want to start again? \
            <a href="http://127.0.0.1:5000/input"> \
            \
            <button>Start</button> \
                </a> </p> \
            </body> \
            </html>'


@app.route('/gamestart', methods=['GET', 'POST'])
def gamestart():
    playername = session.get("playername")
    remaining = session.get("remaining")
    info = session.get("info")
    checkoutinfo = session.get("checkoutinfo")
    info = "Your remaining score is " + str(remaining)
    checkoutinfo = ""

    if request.method == 'POST': 

        score = int(request.form["new_score"])

        ##There is an issue with remaining > score. 
        ##Need to pass through the new remaining score before the logic, otherwise it's always true.
        if remaining - score == 1:

            info = "Score bust, throw again. Score is " + str(remaining)

            session["remaining"] = remaining
            session["info"] = info
            session["checkoutinfo"] = checkoutinfo
            return render_template("game.html", playername=playername, remaining=remaining, info=info, checkoutinfo=checkoutinfo)

        if remaining > score:

            remaining -= score
            info = "Your remaining score is " + str(remaining)
            
            if can_checkout(remaining):
                checkoutinfo = "You can checkout"
                
            else: 
                checkoutinfo = "" 

            session["remaining"] = remaining
            session["info"] = info
            session["checkoutinfo"] = checkoutinfo
            return render_template("game.html", playername=playername, remaining=remaining, info=info, checkoutinfo=checkoutinfo)

        if remaining < score:

            if can_checkout(remaining):
                checkoutinfo = "You can checkout"
                
            else: 
                checkoutinfo = "" 
            
            info = "Score bust, throw again. Score is " + str(remaining)

            session["remaining"] = remaining
            session["info"] = info
            session["checkoutinfo"] = checkoutinfo
            return render_template("game.html", playername=playername, remaining=remaining, info=info, checkoutinfo=checkoutinfo)

        if remaining == score:
            info = "You have checked out"


    return render_template("game.html", playername=playername, remaining=remaining, info=info, checkoutinfo=checkoutinfo)

if __name__ == "__main__":
    app.run(debug=True)