# from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    """Get user by name and ask if they want to play a game."""

    player = request.args.get("person")

    adjective = request.args.get("compliment")

    return render_template("compliment.html", person= player, compliment= adjective)

@app.route('/game')
def show_madlib_form():
    """Shows madlib form."""

    answer = request.args.get("gamechoice")

    if answer == "yes":
      return render_template("game.html")

    else:
      return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective= request.args.get("adjective")
    return render_template("madlib.html", color= color, noun=noun,person=person, adjective)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
