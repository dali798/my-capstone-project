import csv
import os
from random import choice, randint

import crud
import model
import server


os.system("dropdb trails")
os.system("createdb trails")

model.connect_to_db(server.app)
model.db.create_all()

# Load trail data from csv file
with open ("trails_data.csv", newline="") as f:
    trails_data = csv.DictReader(f)
    #print(type(trails_data))

    # Create trails, store them in list so we can use them
    trails_in_db = []

    for trail in trails_data:        
        trail_id = trail["trail_id"]
        name = trail["name"]
        park = trail["area_name"]
        city = trail["city_name"]
        state = trail["state_name"]
        coordinates = trail["_geoloc"]
        popularity = trail["popularity"]
        length = trail["length"]
        elevation = trail["elevation_gain"]
        difficulty = trail["difficulty_rating"]
        avg_rating = trail["avg_rating"]
        features = trail["features"]
        activities = trail["activities"]
        #print(name, " : ", park)
        #print(features)
        db_trail = crud.create_trail(
            trail_id, name, park, city, state, coordinates, popularity, length, elevation, difficulty, avg_rating, features, activities
            )

        trails_in_db.append(db_trail)

        # Create 10 users; each user will make 10 ratings
        # for n in range(1, 11):
        #     first_name = f"Fname{n}"
        #     last_name = f"Lname{n}"
        #     email = f"user{n}@test.com"
        #     password = "test"

        #     user = crud.create_user(first_name, last_name, email, password)

        #     for i in range(10):
        #         random_trail = choice(trails_in_db)
        #         score = randint(1,5)
        #         comment = f"This is my {i}th comment."

        #         crud.create_rating(user, random_trail, score, comment)