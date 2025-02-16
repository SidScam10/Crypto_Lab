n = int(input("Enter n value: "))
a = int(input("Enter Base value:"))

n_minus=n-1
k=0
while n_minus%2==0:
    n_minus//=2
    k+=1

m=(n-1)//(2**k)
T=pow(a,m,n)

def miller_rabin_test(T):
    if T==1 or T==n-1:
        return "Prime"
    
    for i in range(k - 1):
        T = pow(T, 2, n)
        if T == n - 1:
            return "Prime"
        if T == 1:
            return "Composite"
    
    return "Composite"

print(f"{n} is a {miller_rabin_test(T)} number")

