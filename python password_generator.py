import random
import string

def generate_password(length=15):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to meet all requirements.")

    # Required characters
    upper_case = random.choice(string.ascii_uppercase)
    lower_case = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    # Remaining characters
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = random.choices(all_characters, k=remaining_length)

    # Combine all characters
    password_list = [upper_case, lower_case, number, special_char] + remaining_chars
    random.shuffle(password_list)

    # Join to create the final password
    password = ''.join(password_list)
    return password

# Generate and print a password
if __name__ == "__main__":
    print("Your generated password is:", generate_password())