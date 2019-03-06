"""
    Script that corrects the names of the products in the broken database
"""

import json
from json_reading import read_broken_db

def ncorrection(db):
    """
        Function that corrects the 'name' broken fields
        Its parameter is the database with corrupted names
        The 'name' of each json object is read and copied to a new string char by char
        The corrupted characters are corrected when copied to the new string
        The new string is assigned to the json object
        The database with the names corrected is returned
    """
    for l in db:
        name = l['name']
        new_name = ""
        for c in name:
            if c == "æ":
                new_name += 'a'
            elif c == "ß":
                new_name += 'b'
            elif c == "¢":
                new_name += 'c'
            elif c == "ø":
                new_name += 'o'
            else:
                new_name += c
        l['name'] = new_name        
    return db

def main():
    """
        The name correction function is applied and the result is writen in an output json file
    """
    db = ncorrection(read_broken_db())
    with open('output/database/name-corrected.json', 'w') as f:
        json.dump(db, f)
    
if __name__ == "__main__":
    main()
