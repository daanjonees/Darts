from flask import Flask, render_template, request, session, redirect, url_for

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
    session["playername"] = request.form["playername"]
    return redirect(url_for('gamestart'))

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
