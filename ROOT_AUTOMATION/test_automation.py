from subprocess import call
import os

# can also use os but not recommend

# Step 1: Initializing a session ("tutorial.sqlite")
call(["cosmic-ray", "init", "tutorial.toml", "tutorial.sqlite"], shell=True)

# Check that the test suite passes on unmutated code (OPTIONAL)
call(["cosmic-ray", "--verbosity=INFO", "baseline", "tutorial.toml"], shell=True)

# Examining the session with cr-report  (OPTIONAL)
call(["cosmic-ray", "tutorial.sqlite", "--show-pending"], shell=True)

# Step 2: Actual execute the test script:
call(["cosmic-ray", "exec", "tutorial.toml", "tutorial.sqlite"], shell=True)

# Examining the session with cr-report (OPTIONAL)
call(["cosmic-ray", "tutorial.sqlite", "--show-pending"], shell=True)

# Creating an HTML report:
call(["cr-html", "tutorial.sqlite", ">", "report.html"], shell=True)
