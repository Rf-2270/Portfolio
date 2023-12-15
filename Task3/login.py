import getpass

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

def login(username, password):
    with open('passwd.txt', 'r') as file:
        for line in file:
            stored_username, _, stored_password = line.strip().split(':')
            if username == stored_username and rot13(password) == stored_password:
                return True

    return False

if __name__ == "__main__":
    username_to_login = input("User:     ")
    password_to_login = getpass.getpass("Password: ")

    if login(username_to_login, password_to_login):
        print("Access granted.")
    else:
        print("Access denied.")
