# Python 3.9
# Coding: utf-8
###############################################################################
# Creating File Handlers and Modules for Retrieving Information about Insulin #
###############################################################################

# Exercise 1: Creating the JSON molecules data file
# This JSON document stores all the information of previous lab, 
# such as the insulin molecules, the numeric weights of the 
# amino acids and the actual weight of the insulin molecule

# Exercise 2: Creating the JSON file handler module
import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
