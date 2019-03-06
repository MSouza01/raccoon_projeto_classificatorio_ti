"""
    Script that corrects the entire database, applying all three correction funtions from the other scripts
"""

import json
from json_reading import read_broken_db
from name_correction import ncorrection
from price_correction import pcorrection
from quantity_correction import qcorrection

def correction(db):
    """
        Function that corrects the database completely
        The parameter is the broken database
        The corrected database is returned
    """
    db = ncorrection(db)
    db = pcorrection(db)
    db = qcorrection(db)
    return db

def main():
    """
        The correction functions are applied and the corrected database is writen in an output json file
    """
    db = correction(read_broken_db())
    with open('output/database/corrected-database.json', 'w') as f:
        json.dump(db, f)
    
if __name__ == "__main__":
    main()
