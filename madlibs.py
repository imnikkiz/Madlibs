from random import choice
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    response = request.args.get("answer")

    if response == "no":
        return render_template("goodbye.html")
    if response == "yes":
        return render_template("game.html")

@app.route('/madlib', methods=['GET', 'POST'])
def show_madlib():
    if request.method == 'POST':
        person = request.form.get("person")
        noun = request.form.get("noun")
        adjective = request.form.get("adjective")
        color = request.form.get("color")
    if request.method == 'GET':
        person = request.args.get("person")
        noun = request.args.get("noun")
        adjective = request.args.get("adjective")
        color = request.args.get("color")
    
    POSSIBLE_MADLIBS = ["madlib.html", "madlib2.html"]

    return render_template(choice(POSSIBLE_MADLIBS), 
        person=person, 
        noun=noun, 
        adjective=adjective, 
        color=color)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
