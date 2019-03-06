"""
    Script that validates the corrected database printing the total values of each product category
"""

import json
from json_reading import read_corrected_db
from decimal import Decimal

def get_categories(db):
    """
        Function that makes a sorted list of the category names from the provided database
        Its parameter is the database, it doesn't matter if it is corrected or not
        The function returns the sorted categories list
    """
    categories = []
    for l in db:
        if l['category'] not in categories:
            categories.append(l['category'])
    categories.sort()
    return categories

def main():
    """
        Validation function that prints the total values of each category from the corrected database
        The print format is like 'category name\ttotal category value'
        The corrected database is read and it is made a categories list
        For each category in the list, it is verified if it matches with each json object's category
        If it matches, the object price times its quantity (price*quantity) is added to the total value of that category
    """
    db = read_corrected_db()
    categories = get_categories(db)
    
    value = 0
    for c in range(len(categories)):
        for l in db:
            if l['category'] == categories[c]:
                # The Decimal is used because there was a precision problem while using float
                value += Decimal(str(l['price'])) * l['quantity']
        """
            The conditions below are used so the appropriate amount of '\t' is used according to the
            category name size
            With this, the results are more readable
        """
        if len(categories[c]) < 8:
            print(categories[c], end="\t\t\t")
        elif len(categories[c]) < 16:
            print(categories[c], end="\t\t")
        else:
            print(categories[c], end="\t")
        """
            It is used '\r\n' so the output can be read properly if it is writen in a file and the file
            is opened with Windows
        """
        print(value, end="\r\n")
            
        value = 0
    
if __name__ == "__main__":
    main()
