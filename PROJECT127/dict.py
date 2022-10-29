import pandas as pd
import matplotlib as plt

df = pd.read_csv("Gravity_cal.csv")

bools = []
for d in df.Distance:
    if d == 100:
        bools.append(True)
    else:
        bools.append(False)

is_dist = pd.Series(bools)
star_dist=df[is_dist]
star_dist.reset_index(inplace=True,drop=True)

gravity_bool = []
for g in star_dist.Gravity:
    if g<=350 and g>= 150:
        gravity_bool.append(True)
    else:
        gravity_bool.append(False)

is_gravity = pd.Series(gravity_bool)
final_stars = star_dist[is_gravity]

final_stars.reset_index(inplace=True,drop=True)
final_stars.to_csv("New_filtered_stars.csv")