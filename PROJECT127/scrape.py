from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")
time.sleep(10)

page = requests.get(start_url)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find('table')
table_rows = star_table[7].find_all['tr']

templist = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    tdtTag = tr.find_all('td')
    row = [i.text.rstrip() for i in tdtTag]
    templist.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for n in range(1, len(templist)):
    Star_names.append(templist[n][1])
    Distance.append(templist[n][3])
    Mass.append(templist[n][5])
    Radius.append(templist[n][6])
    Lum.append(templist[n][6])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')
