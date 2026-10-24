import string
import secrets

def password_generator(length=8):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{};:?,"

    # Ensure at least one character from each category
    password = [
       secrets.choice(uppercase),
       secrets.choice(lowercase),
       secrets.choice(digits),
       secrets.choice(special)
    ]

    # Combine all allowed characters
    all_characters = uppercase + lowercase + digits + special

    # Fill the remaining password length
    password.extend(
        secrets.choice(all_characters)
        for _ in range(length - 4)
    )

    # Shuffle characters securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Generate a password
print("Generated password:", password_generator())
