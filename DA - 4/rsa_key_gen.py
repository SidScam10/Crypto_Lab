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

print(f"Private Keys: ({d},{n})")