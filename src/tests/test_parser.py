
# Import necessary libraries
import pathlib
import re
import subprocess


# Test help option to make sure it returns expected output
def test_help_option():
    # Get path to main.py file
    path: str = str(pathlib.Path(__file__).parent.resolve()) +\
        "/../main.py"
    # Call main.py with help option and capture output
    output = subprocess.check_output(
        ['python', path, '-h'],
        universal_newlines=True)
    # Check if expected output is present
    assert 'usage:' in output
    assert '-n' in output
    assert '-a' in output
    assert '-abc' in output
    assert '-num' in output
    assert '-s' in output

# Test if generated password contains all possible characters


def test_generate_password_all_characters():
    # Get path to main.py file
    path: str = str(pathlib.Path(__file__).parent.resolve()) +\
        "/../main.py"
    # Call main.py with all characters option and capture output
    output = subprocess.check_output(
        ['python', path, '-a'],
        universal_newlines=True)
    # Check if expected output is present
    assert 'Generated password is:' in output
    # Extract generated password from output
    password = output.split(':', 1)[1].strip()
    # Check if password length is correct and contains all possible characters
    assert len(password) == 12

# Test if generated password contains only alphabetic characters


def test_generate_password_alphabetic_characters():
    # Get path to main.py file
    path: str = str(pathlib.Path(__file__).parent.resolve()) +\
        "/../main.py"
    # Call main.py with alphabetic characters option and capture output
    output = subprocess.check_output(
        ['python', path, '-abc'],
        universal_newlines=True)
    # Check if expected output is present
    assert 'Generated password is:' in output
    # Extract generated password from output
    password = output.split(':', 1)[1].strip()
    # Check if password length is correct and contains only alphabetic
    # characters
    assert len(password) == 12
    assert re.match(r'[A-Za-z]+', password)

# Test if generated password contains only numeric characters


def test_generate_password_numeric_characters():
    # Get path to main.py file
    path: str = str(pathlib.Path(__file__).parent.resolve()) +\
        "/../main.py"
    # Call main.py with numeric characters option and capture output
    output = subprocess.check_output(
        ['python', path, '-num'],
        universal_newlines=True)
    # Check if expected output is present
    assert 'Generated password is:' in output
    # Extract generated password from output
    password = output.split(':', 1)[1].strip()
    # Check if password length is correct and contains only numeric characters
    assert len(password) == 12
    assert re.match(r'[0-9]+', password)

# Test if generated password contains only special characters


def test_generate_password_special_characters():
    # Get path to main.py file
    path: str = str(pathlib.Path(__file__).parent.resolve()) +\
        "/../main.py"
    # Call main.py with special characters option and capture output
    output = subprocess.check_output(
        ['python', path, '-s'],
        universal_newlines=True)
    # Check if expected output is present
    assert 'Generated password is:' in output
    # Extract generated password from output
    password = output.split(':', 1)[1].strip()
    # Check if password length is correct and contains only special characters
    assert len(password) == 12
