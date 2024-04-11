# LockShield Password Manager

# DISCLAIMER:
   This product is meant for educational purposes only.  Any resemblance to real
   persons, living or dead is purely coincidental.  Void where prohibited.  Some
   assembly may be required.  Batteries not included.  Contents may settle during
   shipment.  Use only as directed.  May be too intense for some viewers.  If
   condition persists, consult your physician.  No user serviceable parts inside.
   Breaking seal constitutes acceptance of agreement.  Not responsible for direct,
   indirect, incidental or consequential damages resulting from any defect, error
   or failure to perform.  Slippery when wet.  For office use only.  Substantial
   penalty for early withdrawal.  Do not write below this line.  Your canceled
   check is your receipt.  Avoid contact with skin.  Employees and their families
   are not eligible.  Beware of dog.  Driver does not carry cash.  Limited time
   offer, call now to insure prompt delivery.  Use only in well ventilated area.
   Keep away from fire or flame.  Some equipment shown is optional.  Price does
   not include taxes, dealer prep, or delivery.  Penalty for private use.  Call
   toll free before digging.  Some of the trademarks mentioned in this product
   appear for identification purposes only.  All models over 18 years of age.  Do
   not use while operating a motor vehicle or heavy equipment.  Postage will be
   paid by addressee.  Apply only to affected area.  One size fits all.  Many
   suitcases look alike.  Edited for television.  No solicitors.  Reproduction
   strictly prohibited.  Restaurant package, not for resale.  Objects in mirror
   are closer than they appear.  Decision of judges is final.  This supersedes
   all previous notices.  No other warranty expressed or implied.

![network weights](https://raw.githubusercontent.com/estefanozarate/LockShield/main/rsa-program.png?rar=true)

LockShield Password Manager is a Python application designed to securely store and manage usernames and passwords using robust encryption methods. It provides users with a secure platform to store their login credentials for various websites and retrieve them when needed.

## Features

- **Strong Encryption:** Utilizes RSA encryption to securely store user credentials.
- **Random Password Generation:** Generates strong and randomized passwords for each website.
- **User-Friendly Interface:** Easy-to-use command-line interface for storing and retrieving user credentials.
- **Secure Storage:** Encrypts and stores user credentials locally, ensuring privacy and security.

## Installation

1. Clone the repository:

    $ git clone https://github.com/estefanozarate/LockShield.git

2. Navigate to the project directory:

    $ cd lockshield-password-manager

3. Install the required dependencies:

    $ pip install -r requirements.txt

4. Run the application:

    $ python3 lockshield.py

## Usage

1. Upon running the application, you will be prompted to choose between storing a new user ID or retrieving a stored user ID.
2. If storing a new user ID, enter the name of the website and your username. A secure password will be generated for you.
3. If retrieving a stored user ID, enter the name of the website you want to access, and your decrypted username and password will be displayed.

Enjoy the secure password management provided by LockShield!
