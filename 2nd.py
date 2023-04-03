import argparse
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--motor", default='puls')
args = parser.parse_args()
result = {}
with open(args.file, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=':', quotechar='"')
    title = next(reader)
    data = []
    for index, row in enumerate(reader):
        if row['motor'] == args.motor:
            data.append(list(row.values()))
    for line in data:
        result[line[1]] = [line[4], line[5]]
print(result)
with open('destinations.json', 'w') as res_file:
    json.dump(result, res_file)
