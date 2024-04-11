import random
import time
import rsa 
import base64
import os
import json
from termcolor import colored




ascii_art_title = """
 __                        __              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|  \                      |  \             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
| $$      ______   _______| $$   __        ⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀
| $$     /      \ /       | $$  /  \       ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
| $$    |  $$$$$$|  $$$$$$| $$_/  $$       ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
| $$    | $$  | $| $$     | $$   $$        ⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
| $$____| $$__/ $| $$_____| $$$$$$\        ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
| $$     \$$    $$\$$     | $$  \$$\       ⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
 \$$$$$$$$\$$$$$$  \$$$$$$$\$$   \$$       ⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
  ______  __       __          __       __ ⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
 /      \|  \     |  \        |  \     |  \⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|  $$$$$$| $$____  \$$ ______ | $$ ____| $$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
| $$___\$| $$    \|  \/      \| $$/      $$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 \$$    \| $$$$$$$| $|  $$$$$$| $|  $$$$$$$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 _\$$$$$$| $$  | $| $| $$    $| $| $$  | $$
|  \__| $| $$  | $| $| $$$$$$$| $| $$__| $$
 \$$    $| $$  | $| $$\$$     | $$\$$    $$
  \$$$$$$ \$$   \$$\$$ \$$$$$$$\$$ \$$$$$$$
"""


chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", 
         "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
         "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", 
         "3", "4", "5", "6", "7", "8", "9", "!", "\"", "#", "$", 
         "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", 
         ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", 
         "`", "{", "|", "}", "~"]

def get_pw_info():
    """Collects info about the website and creates a randomized password"""
    print(colored("Storing new user...","light_blue"))
    time.sleep(1)
    password =  ""
    web_site = str(input(colored("Enter name of the website: ","light_cyan")))
    username = str(input(colored("Enter your username: ","light_cyan")))
    time.sleep(1)
    for i in range(1,35):
        new_char =  chars[random.randint(1,len(chars))-1]
        password = password + new_char
    print(colored(f"Secure password generated: {password}","light_green"))
    return (web_site, username, password)

def generate_key_pairs():
    """Generates key pairs"""
    if not os.path.exists("public_key.pem") and not os.path.exists("private_key.pem") : 
        public_key, private_key = rsa.newkeys(1024)
        with open("public_key.pem", "wb") as public_file:
            public_file.write(public_key.save_pkcs1("PEM")) #using the standard way 
        with open("private_key.pem", "wb") as private_file:
            private_file.write(private_key.save_pkcs1("PEM"))
        print(colored("Successfully generated keys!","green"))
    else: 
        pass

def get_key_pairs():
    """Accesses the key pairs from where they are stored locally"""
    with open("private_key.pem", "rb") as private_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
    with open("public_key.pem", "rb") as public_file:
        public_key = rsa.PublicKey.load_pkcs1(public_file.read())
    return (private_key, public_key)

def encrypt_message(text_to_encrypt, public_key):
    """Uses the public key to encrypt the username and password"""

    encrypted_message = rsa.encrypt(text_to_encrypt.encode(), public_key)
    return encrypted_message

def decrypt_user_password(text_to_decrypt, pk):
    """Uses the private key to decrypt the username and password"""
    return rsa.decrypt(text_to_decrypt, pk).decode()

def store_password(txt_binary, website):
    """Stores the encrypted username and password to a file, 
    indexed by the unencrypted website name"""

    txt_b64 = base64.b64encode(txt_binary).decode()
    str_to_file = str(website + ":" + txt_b64 + '\n')
    with open("user_password_file.json", "a") as f:
        f.write(str_to_file)

def get_user_password(website):
    """Finds the encrypted username and password based on what website is being input and outputs the b64 version of it"""
    data_user = "password does not exist"
    my_file = open("user_password_file.json", "r")
    for lines in my_file:
        splitted = lines.strip().split(":")
        if splitted[0].upper() == website.upper():
            data_user = splitted[1]
            break
    return data_user

def delete_line_by_first_word(website):
    # Read the content of the file
    with open("user_password_file.json", 'r') as file:
        lines = file.readlines()

    # Filter out lines that don't start with the target word
    filtered_lines = [line for line in lines if not line.strip().startswith(website)]

    # Write the modified content back to the file
    with open("user_password_file.json", 'w') as file:
        file.writelines(filtered_lines)

def recover_user_password(website,user_password, private_key):
    """Decrypts username and password"""
    user_password_binary_mode = base64.b64decode(user_password)
    user_password_plain_text = decrypt_user_password(user_password_binary_mode, private_key) #decrypting by using the rsa_private_key
    user_list = user_password_plain_text.split(":")
    print(colored(
        f"Your login details for {website} are: ", "light_green") +
        colored("Username: ", "light_yellow") +
        colored(f"{user_list[0]} ", "light_green") +
        colored("Password: ", "light_yellow") +
        colored(f"{user_list[1]} ", "light_green"))
    time.sleep(2)
    print(colored("Returning to main menu...","light_blue"))
    time.sleep(1)
    main()

def store_or_retrieve():
    """Asks user if they want to store a new user """
    path = 0
    while path not in range(1,3):
        try:
            path = int(input(colored("1. To store a new user ID: Press 1: \n2. To retrieve a stored user ID: Press 2: ","light_cyan")))
            if path == 1:
                return 1
                break
            elif path == 2:
                return 2
                break
            else:
                print("Enter 1 or 2.")
        except ValueError:
            print("You need to enter 1 or 2.")
        
def store_user(public_key):
    """Collects info about new user, encrypts it and stores it in the file"""
    web_site_name, username, pw = get_pw_info()
    if os.path.exists("user_password_file.json"):
        if get_user_password(web_site_name) == "password does not exist":
            data_to_encrypt = str(username + ":" + pw)
            encryped_username_pw = encrypt_message(data_to_encrypt,public_key)
            store_password(encryped_username_pw, web_site_name)
            print(colored("New user and password successfully ecrypted and stored","light_green"))
            time.sleep(2)
            print(colored("Returning to main menu...","light_blue"))
            time.sleep(1)
            main()
        else:
            confirm_delete = input(colored("That website already has a user stored. Would you like to overwrite with new data? Y/N?","light_red")).lower()
            if confirm_delete.startswith("y"):
                delete_line_by_first_word(web_site_name)
                data_to_encrypt = str(username + ":" + pw)
                encryped_username_pw = encrypt_message(data_to_encrypt,public_key)
                store_password(encryped_username_pw, web_site_name)
                print(colored("New user and password successfully ecrypted and stored","light_green"))
                time.sleep(2)
                print(colored("Returning to main menu...","light_blue"))
                time.sleep(1)
                main()
            else:
                print(colored("New user has not been stored, returning to main menu...","light_magenta"))
                main()

    else:
        data_to_encrypt = str(username + ":" + pw)
        encryped_username_pw = encrypt_message(data_to_encrypt,public_key)
        store_password(encryped_username_pw, web_site_name)
        print(colored("New user and password successfully ecrypted and stored","light_green"))
        time.sleep(2)
        print(colored("Returning to main menu...","light_blue"))
        time.sleep(1)
        main()

def retrieve_user(private_key):
    """Collects name of website and returns decrypted username and password"""
    website_request = str(input(colored("Which website would you like to access?: ","light_cyan")))
    if website_request:
        
        time.sleep(1)
        data_user = get_user_password(website_request)
        if data_user == "password does not exist":
            print(colored(f"Website called: {website_request} not stored in the database, perhaps you misspelled it?","light_red"))
            retrieve_user(private_key)
        else:
            print(colored(f"Retrieving encrypted data for {website_request}","light_blue"))
            recover_user_password(website=website_request, user_password=data_user,private_key=private_key)

def main():
    """Main logic"""
    
    generate_key_pairs()
    private_key, public_key = get_key_pairs()
    if not os.path.exists("user_password_file.json"):
        store_user(public_key)
    print(colored("What would you like to do?","light_magenta"))
    choice = store_or_retrieve()
    if choice == 1:
        store_user(public_key)
    elif choice == 2:
        print(colored("Retrieving stored username and password...","light_blue"))
        retrieve_user(private_key)

if __name__ == "__main__":
    """Run the program"""
    print(colored(ascii_art_title, "yellow"))
    print(colored("Welcome to LockShield Password Manager V.0.3","light_magenta"))
    main()