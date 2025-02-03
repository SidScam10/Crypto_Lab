a=int(input("Enter base: "))
i=int(input("Enter exponent: "))
n=int(input("Enter modulo: "))
i_bin = bin(i)[2:]
print(f"Binary representation of x: {i_bin}")
y=1
print("y=a^x mod n\ta=a^2 mod n")
for bit in i_bin[::-1]:
    if bit=='1':
        y=(a*y)%n
    a=(a*a)%n
    print(f"y={y}\ta={a}")
print(f"Fast Exponentiation Result: {y}")