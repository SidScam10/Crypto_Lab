def format_text(text):
    text=text.upper().replace(" ", "")
    if len(text)%2!=0:
        text+="X"
    return text

def numeric_value(text):
    numbers=[]
    for char in text:
        if char.isalpha():
            numbers.append(ord(char)-ord("A"))
    return numbers

def key_to_matrix(key):
    key=key.upper().replace(" ", "")
    if len(key) < 4:
        print("Key Must be atleast 4 characters long")
        exit()
    key=key[:4]
    key_numbers=numeric_value(key)
    return [[key_numbers[0], key_numbers[1]],[key_numbers[2], key_numbers[3]],]

def num_to_text(num):
    text=""
    for n in num:
        text+=chr(n+ord("A"))
    return text

def mod_inverse(a, m):
    for i in range(1, m):
        if (a*i)%m==1:
            return i
    return None

def matrix_multiply(matrix1, matrix2):
    result=[]
    for i in range(0, len(matrix1), 2):
        row_result=[]
        for j in range(2):
            result_val=sum(matrix1[i+x]*matrix2[x][j] for x in range(2))%26
            row_result.append(result_val)
        result.extend(row_result)
    return result

def inverse_matrix(key_matrix):
    det=(key_matrix[0][0]*key_matrix[1][1]-key_matrix[0][1]*key_matrix[1][0])%26
    inv_det=mod_inverse(det, 26)
    if inv_det is None:
        return None

    adj_mat=[[key_matrix[1][1], -key_matrix[0][1]],[-key_matrix[1][0], key_matrix[0][0]],]

    for i in range(2):
        for j in range(2):
            adj_mat[i][j]=adj_mat[i][j]%26

    inv_mat=[[(inv_det*adj_mat[i][j])%26 for j in range(2)]for i in range(2)]
    return inv_mat

def encrypt(text, key):
    text=format_text(text)
    key_matrix=key_to_matrix(key)
    num=numeric_value(text)
    result_numbers=matrix_multiply(num, key_matrix)
    result_text=num_to_text(result_numbers)
    return result_text

def decrypt(text, key):
    text=format_text(text)
    key_matrix=key_to_matrix(key)
    key_matrix=inverse_matrix(key_matrix)
    if key_matrix is None:
        return "Key matrix is not invertible"
    num=numeric_value(text)
    result_numbers=matrix_multiply(num, key_matrix)
    result_text=num_to_text(result_numbers)
    return result_text

print("Siddhanth Monnappa\t22BCE3061\n")
while(True):
    print("--HILL CIPHER--")
    print("1) Encrypt Text")
    print("2) Decrypt Text")
    print("3) Exit")
    ch=int(input("Enter Choice: "))
    if ch==3:
        break
    key = input("Enter an alphabetic key (min 4 characters): ")
    text = input("Enter the text: ")
    if (ch==1):
        print(f"Ciphertext: {encrypt(text, key)}")
    elif (ch==2):
        print(f"Decrypted Text: {decrypt(text, key)}")
