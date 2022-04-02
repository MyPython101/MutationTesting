# Mutation Testing using Python

## Introduction:

- Python packages that support mutation testing: 
  - mutation-waterfall 0.1.1: Python library for visualizing mutation landscape as waterfall diagram.
  - mutmut 2.4.0: Mutmut is a mutation testing system for Python, with a strong focus on ease of use.
  - mutpy 0.6.1: MutPy is a mutation testing tool for Python 3.3+ source code (no longer support). 
  - mutation 0.4.7: test mutations for pytest. The goal of mutation is to give an idea on how robust, and help improve test suites.
  - cosmic-ray 8.3.5: Cosmic Ray is a mutation testing tool for Python 3. Long-term support and successfully used on a wide variety of projects.

## How to choose a tools (Python):

- Look for how many people are using the tool(s)? (GitHub)
- How many project that it has been successfully used?
- How many extension/support of the tool(s) are available on Python Standard Library (Pypi.org)?
- Is the tool(s) long-term support?
- Is the tool(s) mature?

## Why Cosmic Ray for Python Mutation Testing

- Cosmic Ray has been successfully used on a wide variety of projects ranging from assemblers to oil exploration software.
- There are more than 10 related projects to cosmic-ray for mutation testing.
- Code base, easy to designed complex test cases
- Long term support
- Can be use automation (schedule scripts)
- Retrieved from [1]

## Mutation Testing Overview

- Mutation testing (or Mutation analysis or Program mutation) evaluates the quality of software tests. 
- Mutation testing involves modifying a program's source code or byte code in small ways. 
- A test suite that does not detect and reject the mutated code is considered defective. 
- These so-called mutations, are based on well-defined mutation operators that either mimic typical programming errors 
(such as using the wrong operator or variable name) or force the creation of valuable tests (such as driving each expression to zero). 
- The purpose is to help the tester develop effective tests or locate weaknesses in the test data used for the program or in sections of the code that are seldom or never accessed during execution.
- Retrieved from [3]

## Requirement:

- Knowledge of Python Programming
- Basic Python Command Line
- Python:  an interpreted high-level general-purpose programming language, it can be used for:
  - web development
  - data sciences
  - back-end development
  - software development

## Installation: 
- From Anaconda or Python Console (within PyCharm IDE)
```bash
pip install cosmic-ray
```
- [video](#)

## Implementation

Step that perform a mutation testing using Cosmic Ray:
- Navigate to the source file
- Create configuration file
- Initialize a session (create a SQL file)
- Check that the test suite passes on unmutated code
- 

## Source module and tests

- Mutation testing works by making small mutations to the code under test (CUT) and then running a test suite over the mutated code. 
- For this tutorial, then, we’ll need to create our CUT and a test suite for it. 
  - Creating a new directory which will contain the CUT, the tests, and eventually the Cosmic Ray data. 
  - Refer to this directory as ROOT (or $ROOT if using shell code).

## Template for mutation testing

```bash
cd ROOT_AUTOMATION

# Create a new configuration file
cosmic-ray new-config tutorial.toml

# The first step in a full testing run, then, is to initialize a session:
cosmic-ray init tutorial.toml tutorial.sqlite

# You can use the baseline command to check that the test suite passes on unmutated code:
cosmic-ray --verbosity=INFO baseline tutorial.toml

# Examining the session
cr-report tutorial.sqlite --show-pending

# Execute
cosmic-ray exec tutorial.toml tutorial.sqlite

# HTML report
cr-html tutorial.sqlite > report.html
```

Please refer to [4] for more details.

## Live Demonstration:

[Live Video](https://drive.google.com/file/d/1SnaSN7J7FXdmuhVTPIp7Jbwr0xW8_pGe/view?usp=sharing)

## Automation:
```python
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
```

## Material:
- All the script can be found at [GitHub]()

## Technology
List of technology
- Python 
- Object Oriented Design
- PyCharm IDE

## References
- [Python MutPy](https://github.com/mutpy/mutpy#:~:text=MutPy%20is%20a%20mutation%20testing%20tool%20for%20Python,coverage%20analysis.%20Mutation%20testing%20From%20article%20at%20Wikipedia%3A?msclkid=34e08178b28611ec883cce2f63a34c67) [3]
- [Mutation Testing with Python](https://medium.com/analytics-vidhya/unit-testing-in-python-mutation-testing-7a70143180d8) [2]
- [Python Standard Library](https://pypi.org/) [1]
- [Cosmic Ray Documentation](https://cosmic-ray.readthedocs.io/en/latest/tutorials/intro/index.html) [4]

