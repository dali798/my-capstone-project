"""Server for national park hiking trails app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
# Required to use Flask sessions
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
#app.jinja_env.auto_reload = True



@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/trails")
def all_trails():
    """View all trails"""

    trials = crud.get_trail()
    return render_template("all_trails.html", trails = trails)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_debugger=True,
    )