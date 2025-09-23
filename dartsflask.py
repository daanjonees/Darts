from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev"  

def can_checkout(rem):
    return bool((rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)))

class Players:
    def __init__(player, name, score):
        player.name = name
        player.score = score

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
                <form action="/gamestart" method="POST"> \
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
    #return redirect(url_for('gamestart'))

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