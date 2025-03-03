def fast_expo(a, x, n):
    x_bin=bin(x)[2:]
    y=1
    for bit in x_bin[::-1]:
        if bit=='1':
            y=(y*a)%n
        a=(a*a)%n
    return y

def elgamal_encrypt(q, alpha, Xa, k, M):
    Ya=fast_expo(alpha, Xa, q)
    K=fast_expo(Ya, k, q) 
    C1=fast_expo(alpha, k, q)
    C2=(K*M)%q
    return Ya, C1, C2

def elgamal_decrypt(q, Xa, C1, C2):
    K=fast_expo(C1, Xa, q)
    K_inv=pow(K,-1,q)
    plaintext=(C2*K_inv)%q
    return plaintext

q=int(input("Enter q: "))
alpha=int(input("Enter alpha: "))
Xa=int(input("Enter Xa: "))
k=int(input("Enter k: "))
M=int(input("Enter plaintext: "))
    
Ya, C1, C2=elgamal_encrypt(q, alpha, Xa, k, M)
decrypted_text=elgamal_decrypt(q, Xa, C1, C2)
print(f"\nYa: {Ya}\nCi: ({C1},{C2})")
print(f"Decrypted Text: {decrypted_text}")