def caesar(text, key, chk):
    result=""
    for i in text:
        if i==' ':
            result+=' '
            continue
        if chk == 'e':  
            result+=chr((ord(i)+key-97)%26+97)
        elif chk=='d':
            result+=chr((ord(i)-key-97)%26+97)
    return result

print("Siddhanth Monnappa\t22BCE3061")
while(True):
    print("--CAESAR CIPHER--")
    print("1) Encrypt Text")
    print("2) Decrypt Text")
    print("3) Exit")
    ch=input("Enter your choice: ")
    if ch=='3':
        break
    text=input("Enter PlainText: ")
    text=text.lower()
    key=int(input("Enter Key: "))
    if ch=='1':
        print(f"Caesar Cipher: {caesar(text, key, 'e')}")
    elif ch=='2':
        print(f"Decyphered PlainText: {caesar(text, key, 'd')}")
