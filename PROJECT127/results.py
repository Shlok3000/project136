import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("New_filtered_stars.csv")

name = df["Star_name"].to_list()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
dist = df["Distance"].tolist()
gravity = df["Gravity"].tolist()

plt.figure(figsize=(10,5))
plt.title("Stars Solar Mass")
plt.bar(name[0:9], mass[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars Solar Radius")
plt.bar(name[0:9], radius[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars Gravity(m/s^2)")
plt.bar(name[0:9], gravity[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars distance")
plt.bar(name[0:9], dist[0:9])

plt.show()