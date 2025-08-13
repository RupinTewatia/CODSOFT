import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generates a random password that guarantees at least one of each selected character type."""

    characters = ""
    password_parts = []

    if use_upper:
        characters += string.ascii_uppercase
        password_parts.append(random.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password_parts.append(random.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password_parts.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password_parts.append(random.choice(string.punctuation))

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    # Fill the rest of the password length
    remaining_length = length - len(password_parts)
    if remaining_length < 0:
        remaining_length = 0
        print("Warning: Password length is shorter than the number of character types selected.")

    password_parts.extend(random.choice(characters) for _ in range(remaining_length))
    random.shuffle(password_parts)

    return "".join(password_parts)