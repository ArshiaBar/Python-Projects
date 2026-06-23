from cryptography.fernet import Fernet

def encrypt(data, key):
    f = Fernet(key)
    encryption = f.encrypt(data.encode())
    return encryption

def decrypt(data, key):
    f = Fernet(key)
    decryption = f.decrypt(data).decode()
    return decryption

key = Fernet.generate_key()

while True:
    print("(E)ncryption or (D)ecryption or E(x)it?")
    choice = input("choice: ").lower()
    if choice == 'e':
        data = input("data: ")
        encryption = encrypt(data, key).decode()
        print(f"encryption: {encryption}")
        print(f"key: {key.decode()}")
    elif choice == 'd':
        data = input("data: ")
        dkey = input("key: ")
        if dkey== key.decode():
            ddata = decrypt(data.encode(),key)
            if ddata is not None:
                print(f"decryption: {ddata}")
            else:
                print("failure...")
        else:
            print("Invalid key")
    elif choice == 'x':
        break
    else:
        print("Invalid")