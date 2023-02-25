import json
import os

path = os.getcwd() + '//data'
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

fileName = path + '//' + 'demofile.json'
with open(fileName, 'w') as writeFile:
    json.dump(jsonData, writeFile)
