print("Siddhanth Monnappa\t22BCE3061\n")

A=int(input("Enter A 8-Bit Hex Value: "),16)
B=int(input("Enter B 8-Bit Hex Value: "),16)
C=int(input("Enter C 8-Bit Hex Value: "),16)
D=int(input("Enter D 8-Bit Hex Value: "),16)

print("\n-MD5 Round Function Values-\n")
F=(B & C) | (~B & D) & 0xFFFFFFFF
G=(B & D) | (C & ~D) & 0xFFFFFFFF
H=B ^ C ^ D & 0xFFFFFFFF
I=C ^ (B | ~D) & 0xFFFFFFFF

print(f"F Function Result: {F:08X}")
print(f"G Function Result: {G:08X}")
print(f"H Function Result: {H:08X}")
print(f"I Function Result: {I:08X}")