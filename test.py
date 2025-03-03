def playfair(key_matrix,d):
    a,b=d
    row_a,col_a=divmod(key_matrix.index(a),5)
    row_b,col_b=divmod(key_matrix.index(b),5)

    if row_a==row_b:
        col_a=(col_a+1)%5
        col_b=(col_b+1)%5
    elif col_a==col_b:
        row_a=(row_a+1)%5
        row_b=(row_b+1)%5
    else:
        col_a,col_b=col_b,col_a
    
    return key_matrix[row_a*5+col_a]+key_matrix[row_b*5+col_b]

text=input("Enter plaintext: ")
key=input("Enter key: ")
alpha='abcdefghjklmnopqrstuvwxyz'
key_matrix=[]
text=text.lower().replace(' ','').replace('i','j')
key=key.lower().replace(' ','').replace('i','j')
for alp in key+alpha:
    if alp not in key_matrix:
        key_matrix.append(alp)
if len(text)%2!=0:
    text+='x'
diagraph=[text[i:i+2] for i in range(0,len(text),2)]
res=""
for d in diagraph:
    res+=playfair(key_matrix,d)
print(res)