def add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1,y1=P
    x2,y2=Q
    if x1==x2 and y1==p-y2:
        return None
    if x1==x2 and y1==y2:
        if y1==0:
            return None
        l=((3*x1*x1+a)*pow(2*y1,p-2,p))%p
    else:
        l=((y2-y1)*pow(x2-x1,p-2,p))%p
    x3=(l*l-x1-x2)%p
    y3= (l*(x1-x3)-y1)%p

    return (x3, y3)

def mul(P, k, a, p):
    R=None
    Q=P
    while k:
        if k&1:
            R=add(R, Q, a, p)
        Q=add(Q, Q, a, p)
        k>>=1

    return R

def ecc_encrypt(P, M, a, b, G, nB, k):
    public_key=mul(G, nB, a, P)
    shared_secret=mul(public_key, k, a, P)

    C1=mul(G, k, a, P)
    C2=add(M, shared_secret, a, P)

    return public_key, (C1, C2)

print("Siddhanth Monnappa\t22BCE3061\n")
P=int(input("Enter P (Prime Modulus): "))
M=list(map(int, input("Enter M (Message Point) Values: ").split()))
a=int(input("Enter a (Curve Parameter a) value: "))
b=int(input("Enter b (Curve Parameter b) value: "))
G=list(map(int, input("Enter G (Base Point) values: ").split()))
nB=int(input("Enter nB (Private key) value: "))
k=int(input("Enter k (Randomisation) value: "))

public_key,cipher_text=ecc_encrypt(P, M, a, b, G, nB, k)

print("\n-ECC Encryption Results-\n")
print(f"Public Key: {public_key}")
print(f"Cipher Text: {cipher_text}")