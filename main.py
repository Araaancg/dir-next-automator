from utils.functions.handleJson import getData
from utils.functions.handleFiles import iterateProjectStructure
from utils.functions.toCamelCase import toCamelCase


proyectPath = './tests/src'

structure = getData("./toCreate.json")
iterateProjectStructure(structure["src"], proyectPath)