import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
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

    remaining_length = length - len(password_parts)
    if remaining_length < 0:
        remaining_length = 0
        print("Warning: Password length is shorter than the number of character types selected.")

    password_parts.extend(random.choice(characters) for _ in range(remaining_length))
    random.shuffle(password_parts)

    return "".join(password_parts)

def get_user_input():
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return None
        
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        return length, use_upper, use_lower, use_digits, use_symbols
    except ValueError:
        print("Invalid input. Please enter a number for length.")
        return None

def main():
    user_input = get_user_input()
    if user_input:
        length, use_upper, use_lower, use_digits, use_symbols = user_input
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if password:
            print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()