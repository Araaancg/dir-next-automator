import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(SCRIPT_DIR, "toCreate.json")
TESTS_PATH = os.path.join(SCRIPT_DIR, "tests", "src")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "assets", "temp")
ASSETS_PATH = os.path.join(SCRIPT_DIR, "assets")