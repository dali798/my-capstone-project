"""Server for national park hiking trails app."""

from flask import Flask, render_template, request, flash, session, redirect
#from model import connect_to_db


from jinja2 import StrictUndefined

app = Flask(__name__)
# Required to use Flask sessions
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True



@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )