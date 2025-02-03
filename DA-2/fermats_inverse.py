def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter a value: "))
n=int(input("Enter n value: "))
for i in range(2,n//2):
    if(n%i==0):
        print("Not possible using Fermat's Inverse")
        exit()
if(gcd(a,n)!=1):
    print("Not possible using Fermat's Inverse")
    exit()
a_inv=a**(n-2)%n
print(f"Multiplicative Inverse using Fermat's Theorm: {a_inv}")
