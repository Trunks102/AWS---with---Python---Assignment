import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the email validation
email = "example@example.com"
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
    
def validate_mobile(mobile):
pattern = r'^[6-9]\d{9}$'
if re.match(pattern, mobile):
    return True
else:
    return False

mobile_number = "7200139521"
if validate_mobile(mobile_number):
    print(f"{mobile_number} is a valid mobile number.")
else:
    print(f"{mobile_number} is not a valid mobile number.")