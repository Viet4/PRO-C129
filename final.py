import csv

dataset1 = []
dataset2 = []

with open("venv/scrapper.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("venv/data_edit.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers_1 = dataset1[0]
headers_2 = dataset2[0]
star_data_1 = dataset1[1:]
star_data_2 = dataset2[1:]

#headers = headers_1 + headers_2
headers = headers_1
star_data = []

for i in star_data_1:
    star_data.append(i)

for i in star_data_2:
    star_data.append(i)

with open("venv/final.csv", "a+", newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)