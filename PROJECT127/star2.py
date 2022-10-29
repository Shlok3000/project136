import csv

stardata1 = []
stardata2 = []

with open("bright_stars.csv", "r") as o:
    q = csv.reader(o)
    for v in q:
        stardata1.append(v)

with open("star_data.csv", "r") as l:
    b = csv.reader(l)
    for u in b:
        stardata2.append(u)

header1 = stardata1[0]
header2 = stardata2[0]

brightdata1 = stardata1[1:]
brightdata2 = stardata2[1:]

headers = header1 + header2

brightdata = []

for index, item in enumerate(brightdata1):
    brightdata.append(brightdata1[index]+brightdata2[index])

with open("last.csv", "a+") as b:
    g = csv.writer(b)
    g.writerow(headers)
    g.writerows(brightdata)