import csv

data = []

with open("dwarf_stars.csv", 'r') as e:
    y = csv.reader(e)
    for i in y:
        data.append(i)

headers = data[0]
star_data = data[1:]

for m in star_data:
    m[2] = m[2].lower()

star_data.sort(key=lambda star_data:star_data[2])

with open("star_data.csv", "a+") as s:
    z = csv.writer(s)
    z.writerow(headers)
    z.writerows(star_data)