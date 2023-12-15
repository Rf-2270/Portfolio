def delete_user(username):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    found = False
    with open('passwd.txt', 'w') as file:
        for line in lines:
            if not line.startswith(f"{username}:"):
                file.write(line)
            else:
                found = True

    if found:
        print("User Deleted.")
    else:
        print("User not found.")


if __name__ == "__main__":
    username_to_delete = input("Enter username: ")
    delete_user(username_to_delete)
