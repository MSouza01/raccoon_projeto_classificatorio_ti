"""
    Script with functions for reading the database json files
"""

import json

def read_broken_db():
    """
        Function that reads the broken database json file and returns a list os json objects
    """
    with open('input/broken-database.json', 'r') as f:
        db = json.load(f)
    return db
    
def read_corrected_db():
    """
        Function that reads the corrected database json file and returns a list of json objects
    """
    with open('output/database/corrected-database.json', 'r') as f:
        db = json.load(f)
    return db
