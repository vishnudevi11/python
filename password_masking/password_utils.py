from cryptography.fernet import Fernet


def load_key():
    return open("secret.key","r").read()

# Encrypt the plain password

def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the password and return a protected string
def decrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.decrypt(password.encode())