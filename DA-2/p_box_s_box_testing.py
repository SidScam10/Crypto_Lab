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

bits = list(map(int, input("Enter 8 bits: ").split()))

p8_table = list(map(int, input("Enter 8 values for P8 Table: ").split()))

s_boxes = []
print("Enter values for S-boxes:")
for i in range(2):
    s_box = []
    for j in range(4):
        s_box.append(list(map(int, input(f"Enter 4 values for S-box {i+1} row {j}: ").split())))
    s_boxes.append(s_box)

permuted_bits = p8_permutation(bits, p8_table)
substituted_bits = s_box_substitution(permuted_bits, s_boxes)  
print(f"Permutation: {permuted_bits}")
print(f"S-box substitution: {substituted_bits}")