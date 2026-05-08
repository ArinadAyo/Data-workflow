import csv

with open('data/sample.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
