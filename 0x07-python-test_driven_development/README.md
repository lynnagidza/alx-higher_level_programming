# Project Tasks

This project consists of several tasks that involve implementing Python functions and writing corresponding test files. Each task has specific requirements and constraints. Read the instructions for each task carefully and follow the provided guidelines.

## Task 0: Add Integer

- Prototype: `def add_integer(a, b=98)`
- Requirements:
  - `a` and `b` must be integers or floats, otherwise raise a TypeError exception.
  - `a` and `b` should be cast to integers if they are floats.
  - Returns the addition of `a` and `b` as an integer.

## Task 1: Divide Matrix Elements

- Prototype: `def matrix_divided(matrix, div)`
- Requirements:
  - `matrix` must be a list of lists of integers or floats, otherwise raise a TypeError exception.
  - Each row of the matrix must have the same size, otherwise raise a TypeError exception.
  - `div` must be a number (integer or float), and it cannot be zero.
  - Divides all elements of the matrix by `div` and rounds the result to 2 decimal places.
  - Returns a new matrix.

## Task 2: Say My Name

- Prototype: `def say_my_name(first_name, last_name="")`
- Requirements:
  - `first_name` and `last_name` must be strings, otherwise raise a TypeError exception.
  - Prints the message "My name is <first name> <last name>".

## Task 3: Print Square

- Prototype: `def print_square(size)`
- Requirements:
  - `size` must be an integer, otherwise raise a TypeError exception.
  - If `size` is less than 0, raise a ValueError exception.
  - Prints a square with the character '#' of size `size`.

## Task 4: Text Indentation

- Prototype: `def text_indentation(text)`
- Requirements:
  - `text` must be a string, otherwise raise a TypeError exception.
  - Prints the text with 2 new lines after each occurrence of '.', '?', and ':'.

## Task 5: Unittests for Max Integer

- Create unittests for the function `def max_integer(list=[])`.
- Use the `unittest` module for writing the tests.
- Store the test files inside a folder named "tests".
- The test file should be executable using the command `python3 -m unittest tests.6-max_integer_test`.

## Task 6: Matrix Multiplication

- Prototype: `def matrix_mul(m_a, m_b)`
- Requirements:
  - `m_a` and `m_b` must be validated with specific requirements.
  - Both `m_a` and `m_b` must be lists of lists of integers or floats.
  - If the requirements are not met, raise the corresponding exceptions.
  - If `m_a` and `m_b` cannot be multiplied, raise a ValueError exception.
  - Perform matrix multiplication and return the result.

## Task 7: Matrix Multiplication with NumPy

- Prototype: `def lazy_matrix_mul(m_a, m_b)`
- Requirements:
  - Use the NumPy module for matrix multiplication.
  - Test cases should be the same as Task 6 but with new exception types/messages.

## Task 8: Print Python Strings

- Prototype: `void print_python_string(PyObject *p)`
- Requirements:
  - Write a C function that prints Python strings according to the provided format.
  - Handle valid strings and display an error message for invalid strings.

## Folder Structure

The folder structure for this project should be as follows:
- project/
    - tests/
        - 0-add_integer.txt
        - 1-matrix_divided.txt
        - 2-say_my_name.txt
        - 3-print_square.txt
        - 4-text_indentation.txt
        - 5-max_integer_test.py
        - 6-matrix_mul.txt
        - 7-lazy_matrix_mul.txt
        - 8-print_python_string.txt
    - README.md
    - task0.py
    - task1.py
    - task2.py
    - task3.py
    - task4.py
    - task5.py
    - task6.py
    - task7.py
    - task8.c
    - 102-tests.py


Make sure to follow the folder structure and file naming conventions specified in the instructions.

## Dependencies

- Task 7 requires the installation of NumPy version 1.15.0.

## Testing

To test the implemented functions, run the corresponding test files using the Python unittest framework or execute the provided test scripts.

