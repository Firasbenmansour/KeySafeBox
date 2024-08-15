# PassMan

## Overview

PassMan is a simple and secure password manager application designed to help users manage their passwords efficiently. It allows users to store, retrieve, and manage their passwords in an encrypted database. The application includes features such as password generation, encryption/decryption of password databases, and user-friendly command-line interactions.

## Features

- **Password Generation**: Generate strong and secure passwords based on user preferences.
- **Encryption/Decryption**: Securely encrypt and decrypt password databases using cryptographic methods.
- **Database Management**: Add, delete, and view entries in the password database.
- **User Interaction**: Simple command-line interface for easy interaction.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/PassMan.git
2. Navigate to the project directory:
   ```sh
   cd PassMan
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt

## Usage

1. Run the main script:
   ```sh
   python3 PassMan.py
2.  Follow the on-screen prompts to interact with the password manager.

## File Structure

- **`PassMan.py`**: Main script to run the password manager.
- **`CheckDatabase.py`**: Contains functions to check and manage the password database.
- **`passwordGenerator.py`**: Contains functions to generate secure passwords.
- **`encryptionDecryption.py`**: Contains functions to encrypt and decrypt the password database.
- **`requirements.txt`**: List of required Python packages.

## Encryption Method

The encryption and decryption of the password database are handled using the `cryptography` library. The following methods are used:

### Encryption

- **Symmetric Encryption**: The database is encrypted using AES (Advanced Encryption Standard), a symmetric key encryption algorithm.
- **Key Derivation**: A key is derived from the user's password using a key derivation function (KDF) such as PBKDF2 (Password-Based Key Derivation Function 2). This ensures that the key is both strong and unique.
- **Initialization Vector (IV)**: A unique IV is generated for each encryption operation to ensure that identical plaintexts yield different ciphertexts.

### Decryption

- **Key Derivation**: The same key derivation process is used to regenerate the encryption key from the user's password.
- **Symmetric Decryption**: The database is decrypted using the derived key and the IV, restoring the original data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure to follow the coding guidelines and test your changes before submitting.

## Contact
For any questions or suggestions, please contact firasbenmans@gmail.com.
