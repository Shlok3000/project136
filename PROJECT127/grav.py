import csv
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/c-129-project/main/Processed_data/final_data.csv")

df.drop(['Unnamed: 0'],axis=1,inplace=True)

df["Radius"]=df["Radius"].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius = df['Radius'].tolist()
mass = df["Mass"].tolist()
gravity = []

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = float(radius[i]*6.957e+8)
        mass[i] = float(mass[i]*1.989e+30)

convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g = (mass[index]*G)/((radius[index])**2)
        gravity.append(g)

gravity_calculation(radius,mass)

df["Gravity"] = gravity
df.to_csv("Gravity_cal.csv")