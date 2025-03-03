def gcd(a,b):
        if(b==0):
            return a
        else:
            return gcd(b,a%b)
def totient(n):
    res=1
    for i in range(2,n):
        if(gcd(n,i)==1):
            res+=1
    return res

print("Siddhanth Monnappa\t22BCE3061\n")
p=int(input("Enter p: "))
q=int(input("Enter q: "))
e=int(input('Enter e: '))
n=p*q
phi=(p-1)*(q-1)
if gcd(e,phi)!=1:
    print("Multiplicative Inverse of e does not exist")
    exit()
d=e**(totient(phi)-1)%phi

num=int(input("Enter number of plaintexts: "))
pt=[]
for i in range(num):
    x=int(input("Enter plaintext: "))
    pt.append(x)
cipher_text=[]
for plain_text in pt:
    cipher_text.append(pow(plain_text,e,n))
deciphered_text=[]
for cipher in cipher_text:
    deciphered_text.append(pow(cipher,d,n))
print(f"\nPublic Keys: ({e},{n})")
print(f"Private Keys: ({d},{n})")
print(f"Cipher Text: {cipher_text}")
print(f"Deciphered Text: {deciphered_text}")