from password_utils import encrypt_password
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Key saved to 'secret.key'")

if __name__ == "__main__":
    # Uncomment this only for the first time
    generate_key()
    encrypted_password = encrypt_password("Root")
    print("Encrypted password: ", encrypted_password)