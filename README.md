# StudentsInMLOps

This repository is for my class actvity for MLops and it contains a Python class named `StudentsInMLOps` designed to manage student enrollments and drops in a Machine Learning Operations (MLOps) context. It also includes test cases to verify the functionality of the class and a GitHub Actions workflow for continuous integration.

## Class Methods

- `enrollStudents(int)`: Enrolls a specified number of students.
- `dropStudents(int)`: Drops a specified number of students.
- `getTotalStrength()`: Returns the total number of enrolled students.
- `getClassName()`: Returns the class name (`StudentsInMLOps`).

## Testing

Test cases for the `StudentsInMLOps` class are defined in `test.py`. These test cases ensure that the class methods function correctly and produce the expected results. The tests are automatically executed using GitHub Actions on every push event to the repository.

## Continuous Integration

A GitHub Actions workflow (`ci.yml`) is set up to run on every push event. This workflow performs the following steps:

1. Sets up a Python environment.
2. Installs dependencies specified in `requirements.txt` (pytest).
3. Executes the test cases defined in `test.py`.
4. Provides feedback on the success or failure of the test cases.

