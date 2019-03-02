import json

file = 'delhi_highway.json'
with open(file, "r") as read_file:
    data = json.load(read_file)

coord = []

for line in data['features']:
    coord.append(line['geometry']['coordinates'])
