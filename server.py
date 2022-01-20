"""Server for national park hiking trails app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import os
import ast

from jinja2 import StrictUndefined

app = Flask(__name__)
# Required to use Flask sessions
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
#app.jinja_env.auto_reload = True

# API_KEY = os.environ["WEATHER_KEY"]



@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/trails")
def all_trails():
    """View all trails"""

    trails = crud.get_trails()
    
    return render_template("all_trails.html", trails=trails)


@app.route("/trails/<trail_id>")
def show_trail(trail_id):
    """Show detail of a particular trail""" 

    trail = crud.get_trail_by_id(trail_id)
    # url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={trail.city}"
    # response = requests.get(url)
    # weather_data = response.json()

    return render_template("trails_detail.html", trail=trail)
    

@app.route("/parks/<park>")
def show_park_trails(park):
    """Show all trails of a park"""

    park_trails = crud.get_trails_by_park(park)
    return render_template("all_park_trails.html", park=park, park_trails=park_trails)


@app.route("/parks")
def show_park():
    """Show all parks"""

    parks = crud.get_parks_list()
    parks.sort()
    states = crud.get_states_list()
    states.sort()
    #state = request.args.get("state")
    return render_template("all_parks.html", parks=parks, states=states)


@app.route("/users")
def all_users():
    """View all users"""
    users=crud.get_users()
    return render_template("all_users.html", users=users)



@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user"""

    first_name = request.form.get("first_name")    
    last_name = request.form.get("last_name")    
    email = request.form.get("email")    
    password = request.form.get("password")  

    user = crud.get_user_by_email(email)
   
    if user:
        flash("Can not create and account with existing email.")
    else:
        crud.create_user(first_name, last_name, email, password)
        flash("Account created. Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def log_in():
    """User log in"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered is not correct.")
    else:
        #Storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.first_name}!")

    return redirect("/")


@app.route("/trails/<trail_id>/ratings", methods=["POST"])
def create_rating(trail_id):
    """Create a new rating for the trail"""

    log_in_email = session["user_email"]
    rating_score = request.form.get("rating")


    if log_in_email is None:
        flash("Please log in to rate a trail.")
    elif not rating_score:
        flash("Please select a score for your rating.")
    else:
        user = crud.get_user_by_email(log_in_email)
        trail = crud.get_trail_by_id(trail_id)

        crud.create_rating(user, trail, int(rating_score))
        flash(f"{user.first_name}, you rate this trail {rating_score} out of 5.0!")

    return redirect(f"/trails/{trail_id}")

@app.route("/parks_js")
def test_page():

    #state=request.args.get("state")
    states = crud.get_states_list()
    states.sort()
    return render_template("all_park_js.html", states=states)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_debugger=True,
    )