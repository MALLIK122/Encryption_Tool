from cryptography.fernet import Fernet

# Caesar Cipher
def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fernet Functions
def generate_key():
    key = Fernet.generate_key()
    with open("../keys/keyfile.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    try:
        with open("../keys/keyfile.key", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return generate_key()

def fernet_encrypt(text):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def fernet_decrypt(token):
    key = load_key()
    f = Fernet(key)
    try:
        return f.decrypt(token.encode()).decode()
    except:
        return "Invalid token or wrong key!"

if __name__ == "__main__":
    print("🔐 Encryption/Decryption CLI Tool")
    choice = input("Choose method (caesar/fernet): ").lower()
    action = input("Do you want to (encrypt/decrypt)? ").lower()
    text = input("Enter text: ")

    if choice == "caesar":
        shift = int(input("Enter shift value: "))
        if action == "encrypt":
            print("Result:", caesar_encrypt(text, shift))
        else:
            print("Result:", caesar_decrypt(text, shift))

    elif choice == "fernet":
        if action == "encrypt":
            print("Result:", fernet_encrypt(text))
        else:
            print("Result:", fernet_decrypt(text))
