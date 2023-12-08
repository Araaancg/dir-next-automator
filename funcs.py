import json

def getJson(jsonFile):
    with open(jsonFile, encoding="utf8") as file:
        return json.load(file)

def writeJson(data, filePath):
    with open(filePath, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    
def writeTxt(fileName, text):
    with open(fileName, "w") as file:
        file.write(text)

def capitalizeCamelCase(str):
    newStr = "".join([a.capitalize() for a in str.split("-")])
    return newStr


# USER INTERFACE FUNCTIONS #
