import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Gravity_cal.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
gravity.sort()
radius.sort()
plt.plot(radius,mass)
plt.show()

plt.title("Radius and Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass, gravity)
plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Radius")
plt.show()

plt.scatter(radius,mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()