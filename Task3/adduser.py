import getpass

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result


def add_user(username, real_name, password):
    with open('passwd.txt', 'a') as file:
        file.write(f"{username}:{real_name}:{rot13(password)}\n")
    print("User Created.")


if __name__ == "__main__":
    new_username = input("Enter new username: ")

    with open('passwd.txt', 'r') as file:
        for line in file:
            if line.startswith(f"{new_username}:"):
                print("Cannot add. Most likely username already exists.")
                break
        else:
            new_real_name = input("Enter real name:    ")
            new_password = getpass.getpass("Enter password:     ")
            add_user(new_username, new_real_name, new_password)
