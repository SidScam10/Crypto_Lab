def gcd(a,b):
        if(b==0):
            return a
        else:
            return gcd(b,a%b)
def phi(n):
    res=1
    for i in range(2,n):
        if(gcd(n,i)==1):
            res+=1
    return res

a=int(input("Enter a value: "))
m=int(input("Enter m value: "))

a_inv=a**(phi(m)-1)%m
print(f"Multiplicative Inverse using Euler's Theorm: {a_inv}")