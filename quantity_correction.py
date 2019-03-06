"""
    Script that corrects the quantities of the product in the broken database
"""

import json
from json_reading import read_broken_db

def qcorrection(db):
    """
        Function that corrects the 'quantity' broken fields
        Its parameter is the database with corrupted quantities
        It verifies if there is a 'quantity' field in each json object
        If there isn't, it adds the field with zero
        The database with the quantities corrected is returned
    """
    for l in db:
        if "quantity" not in l:
            l['quantity'] = 0
    return db

def main():
    """
        The quantity correction function is applied and the result is writen in an output json file
    """
    db = qcorrection(read_broken_db())
    with open('output/database/quantity-corrected.json', 'w') as f:
        json.dump(db, f)
    
if __name__ == "__main__":
    main()
