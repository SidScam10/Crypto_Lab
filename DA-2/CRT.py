'''
a1=int(input("Enter a1: "))
a2=int(input("Enter a2: "))
a3=int(input("Enter a3: "))

m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

M=m1*m2*m3
M1=M//m1
M2=M//m2
M3=M//m3

M1_inv = pow(M1, -1, m1)
M2_inv = pow(M2, -1, m2)
M3_inv = pow(M3, -1, m3)

x=(a1*M1*M1_inv + a2*M2*M2_inv + a3*M3*M3_inv)%M
print(f"Value of x: {x}")
'''
n = int(input("Enter the number of equations: "))

a = []
m = []
for i in range(n):
    a.append(int(input(f"Enter a{i+1}: ")))
    m.append(int(input(f"Enter m{i+1}: ")))

M = 1
for mi in m:
    M *= mi

x = 0
for i in range(n):
    Mi = M // m[i]
    Mi_inv = pow(Mi, -1, m[i])
    x += a[i] * Mi * Mi_inv

x = x % M
print(f"The solution x is: {x}")