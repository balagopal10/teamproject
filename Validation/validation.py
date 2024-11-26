import re

#function to validate name

def validate_name(name):
    if not name.isalpha():
        raise ValueError("Name should only contain alphabets.")
    return True

#function to validate age

def validate_age(age):
    if age < 18 or age > 65:
        raise ValueError("Age should be between 18 and 65.")
    return True

#function to validate Date of joining

def validate_doj(doj):
    # Example: Validate date format (YYYY-MM-DD)
    import datetime
    try:
        datetime.datetime.strptime(doj, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Date Of Joining must be in YYYY-MM-DD format.")
    
# Function to validate email format

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)


# Function to validate password format

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+{}[]|:"<>?' for char in password):
        return False
    return True


# Function to validate phone number (assuming Indian phone number format)

def is_valid_phone_number(phone):
    regex = r'^[6-9]\d{9}$'
    return re.match(regex, phone)


# Function to validate non-empty input

def is_valid_input(value):
    return bool(value.strip())
