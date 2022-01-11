"""Models for hiking trails app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user id={self.user_id} email={self.email}>"

class Trail(db.model):
    """A trail"""

    __tablename__ = "Trails"

    trail_id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String)
    park = db.Column(db.String) 
    city = db.Column(db.String) 
    state = db.Column(db.String) 
    popularity = db.Column(db.Float) 
    length = db.Column(db.Float) 
    elevation = db.Column(db.Float)
    difficulty = db.Column(db.Integer) 
    features = db.Column(db.Text) 
    activities = db.Column(db.Text)

    def __repr__(self):
        return f"<Trail trail id={self.trail_id} name={self.name}>"

class Rating(db.model):
    """Return a rating"""

    __tablename__ = "ratings"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    trail_id = db.Column(db.Integer, db.ForeignKey("trails.trail_id"))
    rating = db.Column(db.Float)
    comment = db.Column(db.Text)

    user = db.relationship("User", backref="ratings")
    trail = db.relationship("Trail", backref="ratings")

    def __repr__(self):
        return f"<Rating id={self.id} rating={self.rating}>"

def connect_to_db(flask_app, db.uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db.uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")




