def is_strong_password(password):
    """
    Checks if the password meets basic security rules:
    - At least 8 characters
    - Contains uppercase and lowercase letters
    - Contains at least one digit
    """
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


def create_password():
    while True:
        password = input("Create a password: ")
        if is_strong_password(password):
            print("Password created successfully.\n")
            return password
        else:
            print("Weak password. Try again.")
            print("Password must be at least 8 characters long,")
            print("contain uppercase, lowercase, and a number.\n")


def login_system(stored_password):
    attempts = 3

    while attempts > 0:
        entered_password = input("Enter your password: ")

        if entered_password == stored_password:
            print("Access granted.")
            return
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts left: {attempts}")

    print("Account locked. Too many failed attempts.")


# Main program
user_password = create_password()
login_system(user_password)