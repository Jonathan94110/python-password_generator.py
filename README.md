# Password Generator

## Overview

This is a Python-based **Password Generator** script that creates strong, secure, and random passwords. It ensures that every password contains a mix of:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

The script is simple to use and customizable, making it ideal for generating secure passwords for any purpose.

---

## Features

- Ensures every password meets security requirements (minimum length and character diversity).
- Generates a password with a default length of 15 characters.
- Customizable password length.
- Uses `random` and `string` modules for secure password generation.

---

## Requirements

- Python 3.x

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-generator.git

	2.	Navigate to the project directory:
 cd password-generator

 3. 	3.	Run the script:
    python3 password_generator.py
By default, the script generates a random password of 15 characters. To run the script:
	1.	Open a terminal in the directory where the script is located.
	2.	Run the script:
python3 password_generator.py
    	3.	The output will display your generated password:
        Your generated password is: Ab1$cdEfGh2Ijk

   To customize the password length, modify the generate_password() function call in the script:
   print("Your generated password is:", generate_password(length=20))

   Example Output

Generated passwords are random and unique. Example:
Your generated password is: zJ@7sH8X*qWpB3L
