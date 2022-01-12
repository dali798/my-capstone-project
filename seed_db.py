import csv
import os

import crud
import model
import server


os.system("dropdb ratings")
os.system("createdb ratings")

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
            trail_id, name, park, city, state, popularity, length, elevation, difficulty, avg_rating, features, activities
            )

        trails_in_db.append(db_trail)