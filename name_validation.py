"""
    Script that validates the corrected database printing the sorted product names
"""

import json
from json_reading import read_corrected_db

def main():
    """
        Validation function that prints the products names sorted by category and than by ID
        The corrected database is read with the function 'read_corrected_db' from the 'json_reading' script
        The list of json objects is sorted as described above and the names are printed, one name per line
    """
    db = read_corrected_db()
    db.sort(key=lambda s: s['id'])
    db.sort(key=lambda s: s['category'])
    for l in db:
        """
            It is used '\r\n' so the output can be read properly if it is writen in a file and the file
            is opened with Windows
        """
        print(l['name'], end="\r\n")
    
if __name__ == "__main__":
    main()
