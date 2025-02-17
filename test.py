def caesar(text,key,chk):
    res=""
    for i in text:
        if i==' ':
            res+=' '
        if chk=='e':
            res+=chr((ord(i)+key-97)%26+97)
        elif chk=='d':
            res+=chr((ord(i)-key-97)%26+97)
    return res
text=input("Enter Text: ")
key=int(input("Enter key: "))
print(f"{caesar(text,key,'d')}")