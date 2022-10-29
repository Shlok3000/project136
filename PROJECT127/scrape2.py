from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")
time.sleep(10)

star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')

templist = []

for tr in table_rows:
    tdtTag = tr.find_all('td')
    row = [i.text.rstrip() for i in tdtTag]
    templist.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for n in range(1, len(templist)):
    Star_names.append(templist[n][0])
    Distance.append(templist[n][5])
    Mass.append(templist[n][7])
    Radius.append(templist[n][8])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')