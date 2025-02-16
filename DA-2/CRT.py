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
    try:
        Mi_inv = pow(Mi, -1, m[i])
    except:
        print("Inverse does not exist")
        exit()
    x += a[i] * Mi * Mi_inv

x = x % M
print(f"The solution x is: {x}")