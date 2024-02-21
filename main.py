from utils.functions.handleJson import getData
from utils.functions.handleFiles import iterateProjectStructure


proyectPath = './tests/src'

structure = getData("./toCreate.json")
iterateProjectStructure(structure["src"], proyectPath)