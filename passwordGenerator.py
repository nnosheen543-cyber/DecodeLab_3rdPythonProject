import random
import string

print("=" * 50)
print("      Week 3 Task: RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("\nEnter password length (minimum 6): "))

        if length < 6:
            print("Password length should be at least 6.")
            continue

        special_chars = input("Include special characters? (y/n): ").lower()

        characters = (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits
        )

        if special_chars == 'y':
            characters += "!@#$%^&*"

        # Ensure complexity
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits)
        ]

        if special_chars == 'y':
            password.append(random.choice("!@#$%^&*"))

        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)

        final_password = ''.join(password)

        # Password Strength
        if length < 8:
            strength = "Weak"
        elif length < 12:
            strength = "Medium"
        else:
            strength = "Strong"

        print("\nGenerated Password:", final_password)
        print("Password Strength :", strength)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != 'y':
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")