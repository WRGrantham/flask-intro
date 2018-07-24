"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    'garbage', 'shitbag', 'poopmouth', 'angry bird', 'old gum', 
    'your stepmoms kidney', 'poopy', 'ugly jewlery', 'dirty keyboard',
    'a disposable utensil', 'diabetes']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
	<body>
   Hi! This is the home page.

   <a href="http://localhost:5000/hello"> Hello </a>
   </body>
   </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    # form_string = ""
    # for compliment in AWESOMENESS:
    # 	form_string += '<option value="{}">{}</option>'.format(compliment, compliment)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <input type="radio" name="stuff" value="insult"> Insult
          <input type="radio" name="stuff" value="compliment">Compliment
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    player_choice = request.args.get("stuff")
    

    if player_choice == "compliment":
      stuff = choice(AWESOMENESS)
    if player_choice == "insult":
      stuff = choice(INSULTS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, stuff)



print ("we are in server.py")
print (__name__)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
