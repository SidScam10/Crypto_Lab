def encrypt(key_matrix, d):  
        a, b = d  
        row_a, col_a=divmod(key_matrix.index(a), 5)  
        row_b, col_b=divmod(key_matrix.index(b), 5)  
              
        if row_a==row_b:  
            col_a=(col_a+1)%5  
            col_b=(col_b+1)%5  
        elif col_a==col_b:
            row_a=(row_a+1)%5  
            row_b=(row_b+1)%5  
        else: 
            col_a, col_b=col_b, col_a  
              
        return key_matrix[row_a*5+col_a]+key_matrix[row_b*5+col_b]  

def decrypt(key_matrix, d):  
        a, b = d  
        row_a, col_a=divmod(key_matrix.index(a), 5)  
        row_b, col_b=divmod(key_matrix.index(b), 5)  
              
        if row_a==row_b: 
            col_a=(col_a-1)%5  
            col_b=(col_b-1)%5  
        elif col_a==col_b:
            row_a=(row_a-1)%5  
            row_b=(row_b-1)%5  
        else:
            col_a, col_b=col_b, col_a  
              
        return key_matrix[row_a*5+col_a]+key_matrix[row_b*5+col_b]  
      
print("Siddhanth Monnappa\t22BCE3061\n")
while(True):
    print("--PLAYFAIR ENCRYPTION--")
    print("1) Encrypt Text")
    print("2) Decrypt Text")
    print("3) Exit")
    ch=int(input("Enter Choice: "))
    if ch==3:
        break
    text=input("Enter Text: ")
    key=input("Enter Key: ")  

    alpha='abcdefghiklmnopqrstuvwxyz'  
    key=key.lower().replace(' ', '').replace('j', 'i')  

    key_matrix=''  
    for alp in key+alpha:  
        if alp not in key_matrix:  
            key_matrix+=alp  
          
    text=text.lower().replace(' ', '').replace('j', 'i')  
    if len(text)%2==1:  
        text+='x'  
            
    digraph=[text[i:i+2] for i in range(0, len(text), 2)]  
      
    result=''
    if(ch==1):
        for d in digraph:
            result+=encrypt(key_matrix,d)  
        print("Ciphertext:", result)  
    elif(ch==2):
        for d in digraph:
            result+=decrypt(key_matrix,d)  
        print("Decrypted text:", result)  
    