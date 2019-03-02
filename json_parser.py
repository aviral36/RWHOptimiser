import json
import numpy as np

file = 'delhi_highway.json'
with open(file, "r") as read_file:
    data = json.load(read_file)

coord = []
for line in data['features']:
    coord.append(line['geometry']['coordinates'])
	
new = []
for line in coord:
    for points in line:
        new.append(points)
		
new_np = np.unique(np.array(new),axis=0)
