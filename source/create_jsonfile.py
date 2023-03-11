import json, os
from pathlib import Path

directory_base = str(os.getcwdb())[2:-1]

if os.name == 'nt':
    directory_data = Path(directory_base + '/data')
    directory_source = Path(directory_base + '/source')
else:
    directory_data = directory_base + '/data'
    directory_source = directory_base + '/source'

jsonData = {
    "Name" : "John",
    "Age" : 30,
    "Martial status" : "Married",
    "Children" : ("Ann", "Billy"),
    "Pets" : None,
    "Vehicles" : [
    {"Model" : "BMW 320", "mpg" : 27.5},
    {"Model" : "Toyota Corola", "mpg" : 36.0}
    ]
}

fileName = directory_data + '/demofile.json'
with open(fileName, 'w') as writeFile:
    json.dump(jsonData, writeFile)
writeFile.close()
