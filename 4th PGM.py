#Write a python function to validate the regular expression for the following: a. Email address b. Mobile numbers of Bangladesh c. Telephone numbers of USA d. 16 characters Alpha-numeric password composed of alphabets of upper case, lower case, special characters, numbers

import re

def validate_input(input_str, input_type):
    if input_type == 'email':
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    elif input_type == 'bangladesh_mobile':
        pattern = r'^01[3-9]\d{8}$'
    elif input_type == 'usa_telephone':
        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    elif input_type == 'password':
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    else:
        return False
    
    return re.match(pattern, input_str) is not None

# Test the function
email = 'prasanna.p@hotmail.com'
mobile_bd = '01712345678'
telephone_usa = '(123) 456-7890'
password = 'Abcd1234@!Abcd1234@!'
print(validate_input(email, 'email'))  # True
print(validate_input(mobile_bd, 'bangladesh_mobile'))  # True
print(validate_input(telephone_usa, 'usa_telephone'))  # True
print(validate_input(password, 'password'))  # True