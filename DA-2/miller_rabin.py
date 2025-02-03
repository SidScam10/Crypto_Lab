n=int(input("Enter n value: "))
a=int(input("Enter Base Value: "))
n_minus=n-1
k=0
while(n_minus!=0):
    n_minus=n_minus//2
    k+=1
n_minus=n-1
m=n_minus//(2**k)
T=(a**m)%n
def miller_rabin_test(T):
    if(T==-1 or T==1):
        return "Prime"
    for i in range(1,k):
        print(T)
        T=(T**2)%n
        if(T==-1):
            return "Prime"
        elif(T==1):
            return "Composite"
    return "Composite"
print(f"{n} is a {miller_rabin_test(T)} number")
