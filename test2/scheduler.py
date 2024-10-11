from subprocess import call
import os
import time

# can also use os but not recommend
# Create a configuration file manually

# Step 1: Initializing a session ("tutorial.sqlite")
call(["cosmic-ray", "init", "tutorial.toml", "tutorial.sqlite"], shell=True)
time.sleep(1)

# Check that the test suite passes on unmutated code (OPTIONAL)
call(["cosmic-ray", "--verbosity=INFO", "baseline", "tutorial.toml"], shell=True)
time.sleep(1)

# Examining the session with cr-report  (OPTIONAL)
call(["cosmic-ray", "tutorial.sqlite", "--show-pending"], shell=True)
time.sleep(1)

# Step 2: Actual execute the test script:
call(["cosmic-ray", "exec", "tutorial.toml", "tutorial.sqlite"], shell=True)
time.sleep(7)

# Examining the session with cr-report (OPTIONAL)
call(["cosmic-ray", "tutorial.sqlite", "--show-pending"], shell=True)
time.sleep(7)

# Creating an HTML report:
call(["cr-html", "tutorial.sqlite", ">", "report.html"], shell=True)
