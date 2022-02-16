"""Server for national park hiking trails app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db
import requests
import crud
import os
import ast

from jinja2 import StrictUndefined

app = Flask(__name__)
# Required to use Flask sessions
app.secret_key = "dev fghjfjdgfjhhdffghdfhg"
app.jinja_env.undefined = StrictUndefined
#app.jinja_env.auto_reload = True

#source secrets.sh
API_KEY = os.environ["WEATHER_KEY"]



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
    coords = ast.literal_eval(trail.coordinates)
    lat = coords['lat']
    lng = coords['lng']
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lng}"
    response = requests.get(url)
    data = response.json()
    current_weather = data['current']
    temp = current_weather['temp_f']
    condition = current_weather['condition']['text']
    icon = current_weather['condition']['icon']
    wind = current_weather['wind_mph']
    humidity = current_weather['humidity']
    vis = current_weather['vis_miles']
    uv = current_weather['uv']

    return render_template("trails_detail.html", trail=trail, temp=temp, condition=condition, icon=icon, wind=wind, humidity=humidity, vis=vis, uv=uv)


@app.route("/rating.json", methods=['POST'])
def show_ratings():

    log_in_email = session["user_email"]
    rating = request.json['rating']
    comment = request.json['comment']
    trail_id = request.json['trail_id']

    user = crud.get_user_by_email(log_in_email)
    trail = crud.get_trail_by_id(trail_id)
    crud.create_rating(user, trail, int(rating), comment)

    return jsonify({'rating':rating, 'comment':comment, 'trail_id':trail_id})


@app.route("/trails/<trail_id>/map")
def show_trail_map(trail_id):
    """Show map of a particular trail""" 

    trail = crud.get_trail_by_id(trail_id)
    return render_template("show_map.html", trail = trail)


@app.route("/parks")
def show_park():
    """Show all parks"""

    parks = crud.get_parks_list()
    parks.sort()
    states = crud.get_states_list()
    states.sort()
    
    return render_template("all_parks.html", parks=parks, states=states)


@app.route("/parks.json", methods=["GET"])
def test_page():
    
    dic = crud.create_parks_dic()
    
    return jsonify(dic)


@app.route("/parks/<park>")
def show_park_trails(park):
    """Show all trails of a park"""

    park_trails = crud.get_trails_by_park(park)
    return render_template("all_park_trails.html", park=park, park_trails=park_trails)


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
        return redirect("/")
    else:
        #Storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.first_name}!")
        return redirect("/user_profile")


@app.route("/user_profile")
def show_profile():
    log_in_email = session.get('user_email')

    if log_in_email is None:
        flash("Please log in to see user profile.")
        return redirect("/") 
        
    else:
        user = crud.get_user_by_email(log_in_email)
        ratings = crud.get_raings_by_userid(user.user_id)

        return render_template("user_profile.html", user=user, ratings=ratings)  

@app.route("/logout")
def log_out():
    session.pop("user_email", None)
    return redirect("/")

   



if __name__ == "__main__":
    connect_to_db(app)
    app.run()

    # debug=True,