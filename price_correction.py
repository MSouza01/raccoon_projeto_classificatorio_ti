"""
    Script that corrects the prices of the products in the broken database
"""

import json
from json_reading import read_broken_db

def pcorrection(db):
    """
        Function that corrects the 'price' broken fields
        Its parameter is the database with corrupted prices
        The 'price' field is verified in each json object
        If the 'price' is a string instance, it is converted to float and assigned to the json object
        The database with the prices corrected is returned 
    """
    for l in db:
        price = l['price']
        if isinstance(price, str):
            nprice = float(price)
            l['price'] = nprice
    return db

def main():
    """
        The price correction function is applied and the result is writen in an output json file
    """
    db = pcorrection(read_broken_db())
    with open('output/database/price-corrected.json', 'w') as f:
        json.dump(db, f)
    
if __name__ == "__main__":
    main()
