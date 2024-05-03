import csv
import json

def test_csv_columns():
    with open('profiles1.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert len(header) == 12, "CSV file does not contain 12 columns"

def test_csv_rows():
    with open('profiles1.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) >= 900, "CSV file does not contain 900+ rows"


def test_json_properties():
    with open('data.json', 'r') as file:
        data = json.load(file)
        required_properties = ['Givenname', 'Surname', 'Birthday', 'Country'] 
        for prop in required_properties:
            assert prop in data[0], f"JSON file does not contain property: {prop}"


def test_json_rows():
    with open('data.json', 'r') as file:
        data = json.load(file)
        assert len(data) >= 900, "JSON file does not contain 900+ rows"

# Run the tests
test_csv_columns()
test_csv_rows()
test_json_properties()
test_json_rows()