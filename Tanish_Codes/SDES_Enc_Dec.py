def permute(original, permutation):
    return [original[i] for i in permutation]

def left_shift(bits, shift_count):
    return bits[shift_count:] + bits[:shift_count]

def generate_keys(key, P10, P8, LS1, LS2):
    key = permute(key, P10)
    left, right = key[:5], key[5:]
    left, right = left_shift(left, LS1), left_shift(right, LS1)
    key1 = permute(left + right, P8)
    left, right = left_shift(left, LS2), left_shift(right, LS2)
    key2 = permute(left + right, P8)
    return key1, key2

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox(input_bits, sbox):
    row = (input_bits[0] << 1) + input_bits[3]
    col = (input_bits[1] << 1) + input_bits[2]
    return [int(x) for x in format(sbox[row][col], '02b')]

def f_k(bits, key, EP, S0, S1, P4):
    left, right = bits[:4], bits[4:]
    right_expanded = permute(right, EP)
    xor_result = xor(right_expanded, key)
    sbox_output = sbox(xor_result[:4], S0) + sbox(xor_result[4:], S1)
    p4_result = permute(sbox_output, P4)
    return xor(left, p4_result) + right

def sdes_encrypt_decrypt(text, key1, key2, IP, IP_inv, EP, S0, S1, P4, mode='encrypt'):
    text = permute(text, IP)
    if mode == 'encrypt':
        text = f_k(text, key1, EP, S0, S1, P4)
        text = text[4:] + text[:4]
        text = f_k(text, key2, EP, S0, S1, P4)
    else:
        text = f_k(text, key2, EP, S0, S1, P4)
        text = text[4:] + text[:4]
        text = f_k(text, key1, EP, S0, S1, P4)
    return permute(text, IP_inv)

def get_permutation(prompt, length):
    return list(map(lambda x: int(x) - 1, input(prompt).split()))

def get_sbox_values():
    sbox = []
    for i in range(4):
        row = list(map(lambda x: int(x, 2), input(f"Row {i}: ").split()))
        sbox.append(row)
    return sbox

print("Enter IP permutation (e.g., 1 5 2 0 3 7 4 6):")
IP = get_permutation("> ", 8)
print("Enter IP⁻¹ permutation (e.g., 3 0 2 4 6 1 7 5):")
IP_inv = get_permutation("> ", 8)
print("Enter EP permutation (e.g., 3 0 1 2 1 2 3 0):")
EP = get_permutation("> ", 8)
print("Enter P4 permutation (e.g., 1 3 2 0):")
P4 = get_permutation("> ", 4)

print("Enter S0 values (4 rows, space-separated):")
S0 = get_sbox_values()
print("Enter S1 values (4 rows, space-separated):")
S1 = get_sbox_values()

print("Enter P10 permutation (e.g., 2 4 1 6 3 9 0 8 7 5):")
P10 = get_permutation("> ", 10)
print("Enter P8 permutation (e.g., 5 2 6 3 7 4 9 8):")
P8 = get_permutation("> ", 8)
LS1 = int(input("Enter number of left shifts for LS1 (e.g., 1): "))
LS2 = int(input("Enter number of left shifts for LS2 (e.g., 3): "))

key = list(map(int, list(input("Enter 10-bit key (e.g., 1010000010): "))))
plaintext = list(map(int, list(input("Enter 8-bit plaintext (e.g., 10101010): "))))

key1, key2 = generate_keys(key, P10, P8, LS1, LS2)
ciphertext = sdes_encrypt_decrypt(plaintext, key1, key2, IP, IP_inv, EP, S0, S1, P4, mode='encrypt')
decrypted_text = sdes_encrypt_decrypt(ciphertext, key1, key2, IP, IP_inv, EP, S0, S1, P4, mode='decrypt')

print("Plaintext:    ", plaintext)
print("Ciphertext:   ", ciphertext)
print("Decrypted Text:", decrypted_text)