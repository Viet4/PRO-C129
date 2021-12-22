import csv
import pandas as pd
import numpy as np

df = pd.read_csv("venv/data.csv")

df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

data = df.to_numpy()

headers = ["Name", "Distance", "Mass", "Radius"]
star_data = data[0:]

for datapoint in star_data:
    datapoint[2] = float(datapoint[2]) * 0.102763
    datapoint[3] = float(datapoint[3]) * 0.000954588

with open("venv/data_edit.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)