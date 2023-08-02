print("Welcome to cryptography")
def main():
    print("choose one option")
    choice = int(input("1. encrpypt \n2. decrypt"))
    if(choice == 1):
        encryption()
    elif(choice == 2):
        decryption()
    else:
        print("Wrong choice")
    
def encryption():
    print("encryption started")
    msg = input("choose a word to encrypt")
    key = int(input("enter a key (1-94)"))
    encrypted_text = ""
    for i in range(len(msg)):
        temp = (ord(msg[i]) + key)
        if(temp > 126):
            temp = temp - 127 + 32
        encrypted_text = encrypted_text + chr(temp)
        print("encrypted: "+encrypted_text)
        main()
    
def decryption():
    print("decryption started")
    encrp_text = input("enter encrypted text")
    decrp_key = int(input("enter a key (1-94)"))
    decrp_text = ""
    for i in range(len(encrp_text)):
        temp = (ord(encrp_text[i]) - decrp_key)
        if(temp < 32):
            temp = temp + 127 - 32
            decrp_text = decrp_text + chr(temp)
    print("decrypted text: "+decrp_text)
if __name__ == "__main__":
    main()


