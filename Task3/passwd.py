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

def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    found = False
    with open('passwd.txt', 'w') as file:
        for line in lines:
            if line.startswith(f"{username}:"):
                _, real_name, stored_password = line.strip().split(':')
                if rot13(current_password) == stored_password:
                    file.write(f"{username}:{real_name}:{rot13(new_password)}\n")
                    found = True
                else:
                    print("Current Password is invalid.")
            else:
                file.write(line)

    if found:
        print("Password changed.")
    else:
        print("User not found.")

if __name__ == "__main__":
    username_to_change = input("User:             ")
    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password:     ")
    confirm_password = getpass.getpass("Confirm:          ")

    if new_password == confirm_password:
        change_password(username_to_change, current_password, new_password)
    else:
        print("Passwords do not match.")
