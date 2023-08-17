#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
app = Flask("__name__")


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=None)
