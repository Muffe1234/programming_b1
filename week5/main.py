import password_functions
import random

print("Password Validator")
print("------------------")
password = input("Enter a password: ")
print("1. Check if password is at least 8 characters long")
print(password_functions.check_min_length(password))
print("2. Check if password has at least one uppercase letter")
print(password_functions.has_uppercase(password))
print("3. Check if password has at least one digit")
print(password_functions.has_digit(password))
print("4. Check if password has at least one special character")
print(password_functions.has_special_char(password))
print("5. Check if password is valid")
print(password_functions.validate_password(password)["is_valid"])
if not password_functions.validate_password(password)["is_valid"]:
    print("Password is invalid")
    print("General Password Suggestion: ", random.choice(password_functions.general_password_suggestions))
print("------------------")
