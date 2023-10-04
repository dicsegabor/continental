Python version = 3.11.5
OS: Manjaro linux

Usage: run install.sh, then run run_tests_generate_report.sh 
Without report creation (from venv) run: 
`cd src/`
`python -m unittest tests.py -v`  

# Project files
* ./project_parameters.json = holds the project specific variables
* ./logs = log directory

* ./install.sh = creates venv and installs the requirements
* ./requirements.in = project requirements
* ./run_tests_generate_report.sh = runs tests and generates report html
* ./src/HTMLTestRunner.py = 3rd party code fixed up for report generation

# Test data description
## Test data sets
* caf_activation: to test that the CAF activates correctly
* caf_false_activation: to test that the CAF doesn't activates incorrectly
* caf_deactivation: to test that the CAF deactivates correctly
* caf_false_deactivation: to test that the CAF doesn't deactivate incorrectly

### caf_activation
* case_0: this case has the max speed limit of the CAF and all the other data set up so it has to activate, and in the second record of the log, it does
* case_1: this case has the max speed limit of the CAF minus 1, to check the correct comparison, otherwise it works like case_0

### caf_false_activation
* case_sensor_input: this case check if the sensor_input_ok isn't true, the CAF doesn't activate
* case_veichle_speed_limit: this case checks if the veichle speed is greater than the CAF max speed limit, then the CAF doesn't activate
* case_veichle_state: this case checks if the veichle state isn't 1, then the CAF doesn't activate

### caf_deactivation
* caf_sensor_input: this case checks if the sensor_input_ok isn't true, then the CAF deactivates
* caf_speed_timeout: this case checks that if the veichle speed is over the CAF max speed limit for more than the timeout, the the CAF deactivates
* case_veichle_state_0: this case checks if the veichle state is 0, then the CAF deactivates
* case_veichle_state_2: this case checks if the veichle state is 2, then the CAF deactivates
* case_veichle_state_7: this case checks if the veichle state is 7, then the CAF deactivates

### caf_false_deactivation
* case_0: this case checks if everything is in order, so the CAF should be active, it doesn't deactivate
* case_1: this case checks if the veichle speed exceeds the CAF max speed limit, but only for timespans below the CAF timeout, then it shouldn't deactivate
