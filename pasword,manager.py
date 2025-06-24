from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

import os

if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

master_pwd = input("what is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|", 1)
                try:
                    decrypted_pwd = fer.decrypt(passw.encode()).decode()
                except Exception as e:
                    decrypted_pwd = f"Error decrypting: {e}"
                print("User:", user, "| Password:", decrypted_pwd)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones? (add/view) press 'q' to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue

