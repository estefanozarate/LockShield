import random
import time
import rsa 
import base64
import json

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
         "w", "x", "y", "z","0", "1", "2", "3", "4", "5", "6", "7",
         "8", "9","!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", 
         "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", 
         "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

def get_pw_info():
    password =  ""
    web_site = str(input("name of the website: "))
    username = str(input("username: "))
    time.sleep(1)
    for i in range(1,20):
        new_char =  chars[random.randint(1,len(chars))-1]
        password = password + new_char
    return (web_site, username, password)


#this function generates the keys
def generate_key_pairs():
    public_key, private_key = rsa.newkeys(1024)
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key.save_pkcs1("PEM")) #using the standard way 
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key.save_pkcs1("PEM"))

def get_key_pairs():
    with open("private_key.pem", "rb") as private_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
    with open("public_key.pem", "rb") as public_file:
        public_key = rsa.PublicKey.load_pkcs1(public_file.read())
    return (private_key, public_key)

def generate_encrypted_file(encrypted_message):
    with open("encrypted_message", "bw") as encrypted_file:
        encrypted_file.write(encrypted_message)

def encrypt_message(text_to_encrypt, public_key):
    encrypted_message = rsa.encrypt(text_to_encrypt.encode(), public_key)
    return encrypted_message

def decrypt_message_from_file(private_key):
    encrypted_message = open("encrypted_message", "rb").read()
    clear_text = rsa.decrypt(encrypted_message, private_key)
    return clear_text.decode()

def decrypt_user_password(text_to_decrypt, pk):
    return rsa.decrypt(text_to_decrypt, pk)

def store_password(txt_binary, website):
    txt_b64 = base64.b64encode(txt_binary).decode()
    str_to_file = str(website + ":" + txt_b64 + '\n')
    with open("user_password_file.json", "a") as f:
        f.write(str_to_file)

def get_user_password(website):
    data_user = ""
    my_file = open("user_password_file.json", "r")
    for lines in my_file:
        splitted = lines.strip().split(":")
        if splitted[0] == website:
            data_user = splitted[1]
            break
    return data_user

def recover_user_password(website,user_password):
    user_password_binary_mode = base64.b64decode(user_password)
    user_password_plain_text = decrypt_user_password(user_password_binary_mode, rsa_keys[0]) #decrypting by using the rsa_private_key
    print(f"{website} ==> {user_password_plain_text}")

if __name__ == "__main__":
    generate_key_pairs()
    web_site_name, username, pw = get_pw_info()
    data_to_encrypt = str(username + "   " + pw)
    rsa_keys = get_key_pairs()
    encryped_username_pw = encrypt_message(data_to_encrypt,rsa_keys[1])
    print("encrypted text: ", encryped_username_pw)
    decrypted_username_pw = rsa.decrypt(encryped_username_pw, rsa_keys[0])
    print("decrypt_text:" , decrypted_username_pw)
    
    #saving {website: username, password}
    store_password(encryped_username_pw, web_site_name)
    time.sleep(1)
    print("getting the password back in plain text!...")
    time.sleep(1)

    website_request = str(input("website's name: "))

    if website_request:
        time.sleep(1)
        s =get_user_password(website_request)

        print(f"{website_request} ==> {s}")
        recover_user_password(website=website_request, user_password=s)
