run_corrections:
	python3 name_correction.py
	python3 price_correction.py
	python3 quantity_correction.py
	python3 database_correction.py
	
run_validations:
	python3 name_validation.py
	python3 value_validation.py
	
run_validations_output:
	python3 name_validation.py > output/validation/name_validation.txt
	python3 value_validation.py > output/validation/value_validation.txt
