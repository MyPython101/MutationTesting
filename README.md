# Mutation Testing using Python

## Introduction

Mutation testing evaluates how well a test suite can detect changes in source code. If a change (mutation) does not alter the test results, the tests may be ineffective.

## Popular Python Tools

- **mutmut**: Easy-to-use mutation testing system.
- **mutation-waterfall**: Visualizes mutation landscapes.
- **mutpy**: (No longer supported) Mutation testing tool for Python.
- **mutation**: Pytest integration for mutation testing.
- **cosmic-ray**: Widely used, long-term support mutation testing tool for Python 3.

## Choosing a Tool

Consider:
- Popularity and usage
- Project history and maturity
- Availability of support/extensions
- Long-term maintenance

## Why Choose Cosmic Ray?

- Used in diverse projects.
- Extensive related projects.
- Supports automated and complex test scenarios.
- Long-term support.

## Overview of Mutation Testing

Mutation testing modifies code to introduce small errors and checks if the test suite can catch them. Effective tests will detect the mutations; if they don’t, the tests need improvement.

## Requirements

- Python programming knowledge.
- Basic command-line skills.
  
## Installation

```bash
pip install cosmic-ray
```

## Implementation Steps

1. Navigate to the source file.
2. Create a configuration file.
3. Initialize a session (SQL file).
4. Check if the test suite passes on un-mutated code.
5. Execute the tests.
6. Examine the session.
7. Generate an HTML report.

## Manual Execution Template

```bash
# Create config file
cosmic-ray new-config tutorial.toml

# Initialize session
cosmic-ray init tutorial.toml tutorial.sqlite

# Check un-mutated code
cosmic-ray --verbosity=INFO baseline tutorial.toml

# Execute tests
cosmic-ray exec tutorial.toml tutorial.sqlite

# Generate HTML report
cr-html tutorial.sqlite > report.html
```

## Automation Example

```python
from subprocess import call

# Initialize session
call(["cosmic-ray", "init", "tutorial.toml", "tutorial.sqlite"], shell=True)

# Execute tests
call(["cosmic-ray", "exec", "tutorial.toml", "tutorial.sqlite"], shell=True)

# Generate HTML report
call(["cr-html", "tutorial.sqlite", ">", "report.html"], shell=True)
```

For more details, refer to the [live demo](https://www.youtube.com/watch?v=zXgSk4M3B38).