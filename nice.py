from random import choice

from flask import Flask, request, render_template


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <a href="/hello"> Hi! This is the home page.</a>
    </html>
    """



@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <div>
          Please select a compliment:<select name="compliment">
          <option value="awesome">awesome</option> 
          <option value="terrific">terrific</option> 
          <option value="fantastic">fantanstic</option> 
          <option value="neato">neato</option> 
          <option value="fantabulous">fantabulous</option> 
          <option value="wowza">wowza</option> 
          <option value="brilliant">brilliant</option> 
          </div> 
          <div> 
          <input type="submit"> 
          </div>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name and ask if they want to play a game."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return render_template("compliment.html", player, compliment)

@app.route('/game')
def show_madlib_form():
    """Shows madlib form."""

    answer = request.args.get("gamechoice")

    if answer == "yes":
      return render_template("game.html")

    elif answer == "yes":
      return render_template("goodbye.html")





if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
