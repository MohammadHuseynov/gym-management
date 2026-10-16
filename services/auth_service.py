import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    return True

def validate_password(password):

    if len(password) < 8:
        return False , "Password should be at least 8 characters long"
    if not re.search(r'[a-zA-Z]', password):
        return False, "Password should contain at least one letter"
    if not re.search(r'[0-9]', password):
        return False, "Password should contain at least one number"
    if not re.search(r'[@&]', password):
        return False, "Password should contain at least one special character : @ or &"
    return True

def is_username_unique(username, existing_users):

    if not username:
        return False , "Username should not be empty!"
    if username in existing_users:
        return False, "This username is already used!"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username should contain only letters, numbers and _ "
    return True
