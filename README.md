# LockShield Password Manager

 __                        __                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|  \                      |  \      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
| $$      ______   _______| $$   __       ⠀⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀
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
 \$$    \| $$$$$$$| $|  $$$$$$| $|  $$$$$$$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 _\$$$$$$| $$  | $| $| $$    $| $| $$  | $$
|  \__| $| $$  | $| $| $$$$$$$| $| $$__| $$
 \$$    $| $$  | $| $$\$$     | $$\$$    $$
  \$$$$$$ \$$   \$$\$$ \$$$$$$$\$$ \$$$$$$$


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
