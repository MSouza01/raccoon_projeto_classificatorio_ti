Raccoon's classificatory project developed by Moacyr Souza

The project's root directory contains two subdirectories:
	> input: contains the provided input file 'broken-database.json'
	> output: contains two subdirectories
		> database: contains the corrected database files
			> corrected-database.json: the database corrected by all three correction functions
			> name-corrected.json: the database with the corrected product names
			> price-corrected.json: the database with the corrected product prices
			> quantity-corrected.json: the database with the corrected product quantities
		> validation: contains the output files from the validation functions
			> name_validation.txt: the output from the first validation function (the names are sorted and than printed)
			> value_validation.txt: the output from the second validation function (the total values of each category are printed)

There are eight files within the root directory:
	> json_reading.py: This script contains the functions used for reading the broken and corrected database files. All the other scripts
	import its functions.

	> name_correction.py: this script contains the function used for correcting the names from the broken database
	> price_correction.py: this script contains the function used for correcting the prices from the broken database
	> quantity_correction.py: this script contains the function used for correcting the quantities from the broken database

	> database_correction.py: this script imports the other three correction functions and corrects database completely

	> name_validation.py: this script contains the validation function that prints the sorted product names
	> value_validation.py: this script contains the validation function that prints the total value of each category

	> Makefile: contains some run commands to make it easier and faster to run all the scripts
		> run_corrections: run all the correction scripts (all the output is writen in the output directory)
		> run_validations: run all the validation scripts (all the output is writen in the terminal)
		> run_validations_output: run all the validation scripts (all the output is writen in the output directory)
