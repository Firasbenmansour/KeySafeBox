import csv
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import base64

# Constants
SALT_SIZE = 16
NUMBER_OF_ITERATIONS = 20
AES_MULTIPLE = 16

def generate_key(password, salt, iterations):
    assert iterations > 0
    key = password.encode() + salt  # Ensure password is bytes
    for _ in range(iterations):
        key = hashlib.sha256(key).digest()
    return key

def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text

def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])
    text = padded_text[:-padding_size]
    return text

def encrypt(plaintext, password):
    salt = get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    iv = get_random_bytes(AES.block_size)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad_text(plaintext, AES_MULTIPLE).encode()  # Ensure plaintext is bytes
    
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext_with_salt = base64.b64encode(iv + salt + ciphertext)
    
    return ciphertext_with_salt.decode()  # Return as string for easy CSV storage

def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    salt = ciphertext[AES.block_size:AES.block_size + SALT_SIZE]
    ciphertext_sans_salt = ciphertext[AES.block_size + SALT_SIZE:]
    
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    padded_plaintext = cipher.decrypt(ciphertext_sans_salt).decode()  # Decrypt and decode
    plaintext = unpad_text(padded_plaintext)
    
    return plaintext

def crypt_csv(src_file, dst_file, password):
    with open(src_file, 'r') as csv_src_file:
        csv_reader = csv.reader(csv_src_file)
        rows = list(csv_reader)
    
    with open(dst_file, 'w') as csv_dst_file:
        csv_writer = csv.writer(csv_dst_file)
        for row in rows:
            encrypted_row = [encrypt(cell, password) for cell in row]
            csv_writer.writerow(encrypted_row)

def decrypt_csv(src_file, dst_file, password):
    with open(src_file, 'r') as csv_src_file:
        csv_reader = csv.reader(csv_src_file)
        rows = list(csv_reader)
    
    with open(dst_file, 'w') as csv_dst_file:
        csv_writer = csv.writer(csv_dst_file)
        for row in rows:
            decrypted_row = [decrypt(cell, password) for cell in row]
            csv_writer.writerow(decrypted_row)