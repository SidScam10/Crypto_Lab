def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter a value: "))
n=int(input("Enter n value: "))
if(gcd(a,n)!=1):
    print("Extended Euclidean's Multiplicative Inverse not possible")
    exit()
r1=n
r2=a
t1=0
t2=1
print(f"r1: {r1}\tr2: {r2}\tt1: {t1}\tt2: {t2}")
while(r2>0):
    q=r1//r2
    r=r1-q*r2
    r1=r2
    r2=r

    t=t1-q*t2
    t1=t2
    t2=t
    print(f"r1: {r1} \tr2: {r2}\tt1: {t1}\tt2: {t2}")

if(r1==1):
    if(t1<0):
        t=t1+t2
    else:
        t=t1

print(f"Multiplicative inverse of {a} mod {n} = {t}")