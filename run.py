import csv

with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
