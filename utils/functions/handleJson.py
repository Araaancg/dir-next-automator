# HANDLING JSON FILES
import json

# GET INFO FROM JSON
def getData(jsonFile):
    with open(jsonFile, encoding="utf8") as file:
        return json.load(file)