def rotr(x, n):
    return (x >> n) | (x << (64 - n)) & 0xFFFFFFFFFFFFFFFF

def shr(x, n):
    return x >> n

def sigma0(x):
    return rotr(x, 1) ^ rotr(x, 8) ^ shr(x, 7)

def sigma1(x):
    return rotr(x, 19) ^ rotr(x, 61) ^ shr(x, 6)

def sha_512_inp_seq(M):
    M_bytes=M.encode('utf-8')
    M_bits=''.join(format(byte, '08b') for byte in M_bytes)
    M_len=len(M_bits)
    
    M_bits+='1'
    while len(M_bits)%1024!=896:
        M_bits+='0'
    
    M_bits+=format(M_len, '0128b')
    print(f"Hex Message of 1024 bits: {hex(int(M_bits, 2))}")

    W=[int(M_bits[i:i+64], 2) for i in range(0, 1024, 64)]
    
    for t in range(16, 80):
        Wt=(sigma1(W[t-2])+W[t-7]+sigma0(W[t-15])+W[t-16]) & 0xFFFFFFFFFFFFFFFF
        W.append(Wt)
    
    return W

print("Siddhanth Monnappa\t22BCE3061\n")
M=input("Enter Message: ")
W=sha_512_inp_seq(M)

print("SHA-512 Input Sequence:")
for t, Wt in enumerate(W):
    print(f"W{t} = {hex(Wt)}")
