import secrets
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Ensure the password includes at least one character from each group.
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars.extend(secrets.choice(all_chars) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def main():
    print("=" * 36)
    print("       PASSWORD GENERATOR")
    print("=" * 36)

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Please enter a number of at least 4.")
                continue
            password = generate_password(length)
            print("\nYour strong password is:", password)
            print("Tip: Store it in a trusted password manager.")
            break
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()
