def p8_permutation(bits, table):
    return [bits[i - 1] for i in table]

def s_box_substitution(bits, s_boxes):
    output = []
    for i in range(2):
        block = bits[i*4:(i+1)*4]
        row = int(f"{block[0]}{block[3]}", 2)
        col = int(f"{block[1]}{block[2]}", 2)
        output.extend(f"{s_boxes[i][row][col]:02b}")
    return list(map(int, output))

bits=[]
for i in range(8):
    bits.append(int(input(f"Enter value for bit {i+1}:")))

p8_table = []
print("Enter values for P8 Table:")
for i in range(8):
    p8_table[i] = int(input("Enter value:"))
    
s_boxes=[]
for i in range(2):
    for j in range(4):
        for k in range(4):
            s_boxes[i][j][k] = int(input(f"Enter value for S-box {i+1} row {j} column {k}:"))

permuted_bits = p8_permutation(bits, p8_table)
substituted_bits = s_box_substitution(permuted_bits, s_boxes)  
print(f"Permutation: {permuted_bits}")
print(f"S-box substitution: {substituted_bits}")