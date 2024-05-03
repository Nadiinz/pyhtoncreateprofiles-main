import csv
import json

csv_file = 'profiles1.csv'
json_file = 'data.json'

data = []

# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Write the JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
    