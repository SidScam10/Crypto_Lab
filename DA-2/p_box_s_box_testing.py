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

p8_table = [3, 5, 2, 7, 4, 8, 6, 1]

s_boxes = [
    [[1, 0, 3, 2],
     [3, 2, 1, 0],
     [0, 2, 1, 3],
     [3, 1, 0, 2]],
    [[0, 1, 2, 3],
     [2, 0, 1, 3],
     [3, 0, 1, 2],
     [2, 1, 0, 3]]
]

bits = [1, 0, 1, 1, 0, 1, 0, 0]

permuted_bits = p8_permutation(bits, p8_table)
substituted_bits = s_box_substitution(permuted_bits, s_boxes)  
print(f"Permutation: {permuted_bits}")
print(f"S-box substitution: {substituted_bits}")