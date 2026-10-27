from flask import Flask 

app = Flask(__name__) "creates a new Flask application instance."


@app.route("/") "defines a route for the root URL ("/") of the application."
def home():     "defines a function that handles requests to the root URL and returns a welcome message."
    return "Welcome to Cafe Rincon"   "prints the welcome message for the cafe's homepage."


@app.route("/about")
def about():
    return "Cafe Rincon is a welcoming neighborhood cafe serving coffee and light bites."  "prints the about message for the cafe's about page."
