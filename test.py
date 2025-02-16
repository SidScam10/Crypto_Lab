PT=input("Enter Plaintext: ")
K=input("Enter Key: ")
n=int(input("Enter n: "))

S=[i for i in range(0,2**n)]
P=[PT[i:i+n] for i in range(0,len(PT),n)]
T=[K[i:i+n] for i in range(0,len(K),n)]

for i in range(len(P)):
    P[i]=int(P[i],2)
for i in range(len(T)):
    T[i]=int(T[i],2)

dif=len(S)-len(T)
for i in range(0,dif):
    T.append(T[i])

print("S:"+ S)
print("T:"+T)

j=0
print("KSA iterations: ")
for i in range(len(S)):
    j=(j+S[i]+T[i]) % len(S)
    S[i],S[j]=S[j],S[i]
    print(i+" "+S)

i=j=t=0
K_stream=[]
print("PRGA iterations: ")
while(i<len(P)):
    i=(i+1) % len(S)
    j=(j+S[i]) % len(S)
    S[i],S[j]=S[j],S[i]
    print(i+" "+S)
    t=(S[i]+S[j]) % len(S)
    K_stream.append(S[t])
print(K_stream)

cipher=[]
for i in range(len(P)):
    cipher.append(P[i]^K_stream[i]) # Decryption: original.append(cipher[i]^K_stream[i])

cipher_text = ""
for i in cipher:
    cipher_text+='0'*(n-len(bin(i)[2:]))+bin(i)[2:]

print("Cipher text: ",cipher_text)