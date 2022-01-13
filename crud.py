"""CRUD operations"""
from model import db, User, Trail, Rating, connect_to_db

def create_user(first_name, last_name, email, password):
    """create and return a new user"""

    user = User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = password
    )
    db.session.add(user)
    db.session.commit

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


def create_trail(trail_id, name, park, city, state, popularity, length, elevation, difficulty, avg_rating, features, activities):
    """create and return a new trail"""

    trail = Trail(
        trail_id = trail_id,
        name = name,
        park = park,
        city = city,
        state = state,
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


def create_rating(rating_id, user_id, trail_id, rating, comment):
    """Create and return a new rating"""

    rating = Rating(
        rating_id = rating_id,
        user_id = user_id,
        trail_id = trail_id,
        rating = rating,
        comment = comment
    )
    db.session.add(rating)
    db.session.commit

    return rating

if __name__ == "__main__":
    from server import app

    connect_to_db(app)

