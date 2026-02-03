def check_min_length(password, min_length=8):
    if len(password) < min_length:
        return False
    return True

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    return any(not char.isalnum() for char in password)

def validate_password(password):
    password_results = {}
    password_results["min_length"] = check_min_length(password)
    password_results["uppercase"] = has_uppercase(password)
    password_results["digit"] = has_digit(password)
    password_results["special_char"] = has_special_char(password)
    password_results["is_valid"] = all(password_results.values())
    return password_results

general_password_suggestions = [
    "Use Diceware method to generate a password",
    "Use a password manager to generate a password",
    "Use a password generator to generate a password",
]

