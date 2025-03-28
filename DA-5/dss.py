def dss(p, q, k, h, priv_key, hm, g):
    pub_key = pow(g, priv_key, p)
    r = pow(g, k, p)%q
    try:
        k_inv=pow(k, -1, q)
    except:
        print("Inverse does not exist")
        exit(0)
    s = (k_inv*(hm+priv_key*r)) % q

    try:
        w=pow(s, -1, q)
    except:
        print("Inverse does not exist")
        exit(0)
        
    u1 = (hm*w)%q
    u2 = (r*w)%q

    v = (pow(g, u1, p)*pow(pub_key, u2, p))%p%q

    if v==r:
        verify="Accepted"
    else:
        verify="Rejected"

    print("\n-DSS Implementation-\n")
    print(f"Public Key: {pub_key}")
    print(f"Signature: (r, s) = ({r}, {s})")
    print(f"Verification Values:   (u1, u2) = ({u1}, {u2})")
    print(f"Verification Status:   {verify}")

print("Siddhanth Monnappa\t22BCE3061\n")

p=int(input("Enter p (Prime Modulus): "))
q=int(input("Enter q (Prime Divisor): "))
k=int(input("Enter k (Randomisation): "))
h=int(input("Enter h (Hash function): "))
priv_key=int(input("Enter Private Key: "))
hm=int(input("Enter Message Hash: "))
g=int(input("Enter g (Base Point): "))

dss(p,q,k,h,priv_key,hm,g)