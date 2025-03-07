#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
app = Flask("__name__")


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return "Hello HBNB!"

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
    bind = "0.0.0.0:8080"
workers = 2
