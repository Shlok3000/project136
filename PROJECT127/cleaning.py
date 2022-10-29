import pandas as pd
import csv

df = pd.read_csv('last.csv')
df.drop(['Star_name',"Distance", 'Mass', 'Radius', 'Luminosity'],axis=1, inplace=True)
final_data = df.dropna()
final_data.reset_index(drop=True,inplace=True)
final_data.to_csv('final.csv')