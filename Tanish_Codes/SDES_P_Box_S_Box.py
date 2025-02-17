def p_box(table, bits):
    permuted_bits = "".join(bits[i - 1] for i in table)
    return permuted_bits


def s_box(table, bits):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    substituted_bits = format(table[row][col], "02b")
    return substituted_bits


print("Name -> Tanishq Anand\nRegistration Number -> 22BCE0508")

p_table = list(map(int, input("Enter The P-Box Table (space-separated) -> ").split()))
s_table = []
print("Enter The S-Box Table (4x4) Row-Wise ->")
for _ in range(4):
    s_table.append(list(map(int, input().split())))

input_bits = input("Enter The Input Bits For P-Box -> ")
p_result = p_box(p_table, input_bits)
print(f"Result -> Permuted Bits [{p_result}]")

s_input_bits = input("Enter The 4 Bits For S-Box -> ")
s_result = s_box(s_table, s_input_bits)
print(f"Result -> Substituted Bits [{s_result}]")