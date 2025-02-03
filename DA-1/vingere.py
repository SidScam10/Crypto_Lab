def generate_key(text, key):
    key=key.upper()
    ext_key=""
    key_index=0

    for char in text:
        if char.isalpha():
            ext_key+=key[key_index%len(key)]
            key_index+=1
        else:
            ext_key+=char
    return ext_key

def vigenere(text, key, chk):
    result=""
    key=generate_key(text, key)

    for i, char in enumerate(text):
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            key_shift=ord(key[i].upper())-ord('A')
            if chk=="e":
                result+=chr((ord(char)-base+key_shift)%26+base)
            else:
                result+=chr((ord(char)-base-key_shift)%26+base)
        else:
            result+=char

    return result

print("Siddhanth Monnappa\t22BCE3061\n")
while(True):        
    print("--VIGENERE ENCRYPTION--")
    print("1) Encrypt Text")
    print("2) Decrypt Text")
    print("3) Exit")
    ch=int(input("Enter Choice: "))
    if ch==3:
        break
    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if ch==1:
        print(f"Encrypted: {vigenere(text,key,"e")}")
    elif ch==2:
        print(f"Decrypted: {vigenere(text,key,"d")}")
