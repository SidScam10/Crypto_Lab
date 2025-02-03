r1=int(input("Enter a value: "))
r2=int(input("Enter b value: "))
s1=1
s2=0
t1=0
t2=1
while(r2>0):
    q=r1//r2

    r=r1-q*r2
    r1=r2
    r2=r

    s=s1-q*s2
    s1=s2
    s2=s

    t=t1-q*t2
    t1=t2
    t2=t
d=r1
s=s1
t=t1

print(f"s value: {s}")
print(f"d value: {d}")
print(f"t value: {t}")