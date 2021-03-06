"""CRUD operations"""
from model import db, User, Trail, Rating, connect_to_db
import csv

def create_user(first_name, last_name, email, password):
    """create and return a new user"""

    user = User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = password
    )
    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """return all users"""

    return User.query.all()


def get_user_by_id(user_id):
    """Return user by id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return user by email"""

    return User.query.filter(User.email == email).first()


def create_trail(trail_id, name, park, city, state, coordinates, popularity, length, elevation, difficulty, avg_rating, features, activities):
    """create and return a new trail"""

    trail = Trail(
        trail_id = trail_id,
        name = name,
        park = park,
        city = city,
        state = state,
        coordinates = coordinates,
        popularity = popularity,
        length = length,
        elevation = elevation,
        difficulty = difficulty,
        avg_rating = avg_rating,
        features = features,
        activities = activities
    )

    db.session.add(trail)
    db.session.commit()

    return trail


def get_trails():
    """return all trails"""

    return Trail.query.all()


def get_trail_by_id(trail_id):
    """return a trail by id"""

    return Trail.query.get(trail_id)

def get_parks_list():
    """Return all park by list"""

    parks_list = []
    trails = get_trails()
    for trail in trails:
        if trail.park not in parks_list:
            parks_list.append(trail.park)

    return parks_list


def get_states_list():
    """Return all states by list"""

    trails = get_trails()
    states_list = []
    for trail in trails:
        if trail.state not in states_list:
            states_list.append(trail.state)
    return states_list
    


def get_trails_by_park(park):
    """Return trais by park"""

    return Trail.query.filter(Trail.park==park).all()



def create_parks_dic():
    trails = get_trails()
    parks_dic = {}
    for trail in trails:
        parks_dic[trail.state] = []

    for trail in trails:         
        if trail.park not in parks_dic[trail.state]:
            parks_dic[trail.state].append(trail.park)
    return (parks_dic)



def create_rating(user, trail, score, comment):
    """Create and return a new rating"""

    rating = Rating(user = user, trail = trail, score = score, comment = comment)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_ratings():
    """return all users"""
    return Rating.query.all()


def get_raings_by_userid(user_id):
    """return ratings by user"""
    return Rating.query.filter(Rating.user_id==user_id).all()


    

if __name__ == "__main__":
    from server import app

    connect_to_db(app)

